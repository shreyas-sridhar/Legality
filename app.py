from flask import Flask, render_template, request, url_for, redirect, session
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from oauthlib.oauth2 import WebApplicationClient
import os
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Google OAuth Configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

@app.route('/')
def home():
    user_info = session.get('user')
    # Placeholder for legal_help data, replace with actual logic
    legal_help = {
        "reference_number": "N/A",
        "timestamp": "N/A",
        "response": "No consultation data available. Please submit a query."
    }
    return render_template('index.html', user=user_info, legal_help=legal_help)


@app.route('/login')
def login():
    # Get Google's authorization endpoint
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Generate authorization URL
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route('/login/callback')
def callback():
    # Get authorization code from Google
    code = request.args.get("code")
    
    # Get token endpoint
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare token request
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    
    client.parse_request_body_response(token_response.text)

    # Fetch user info
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    user_info = userinfo_response.json()
    session['user'] = {
        "id": user_info["sub"],
        "name": user_info["name"],
        "email": user_info["email"],
        "picture": user_info["picture"]
    }

    return redirect(url_for("home"))



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/legal_help')
def legal_help():
    return render_template('legal_help.html')


if __name__ == '__main__':
    app.run(ssl_context="adhoc", debug=True)
