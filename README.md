# Legality
Welcome to the Legal Help Application! This project is a web application built using Flask that allows users to log in using their Google account and access legal consultation information. This README will guide you through the setup and usage of the application, even if you're a novice programmer. (My 5th sem Special topic project built in collab with my team)

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Video Tutorial](#video-tutorial)

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.x
- pip (Python package installer)

## Installation
1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/shreyas-sridhar/Legality.git
   cd Legality
   ```

2. **Install the required packages** using pip:
   ```bash
   pip install Flask requests oauthlib python-dotenv
   ```

## Configuration
To run this application, you need to set up Google OAuth credentials. Follow these steps:

1. **Create a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.

2. **Enable the Google+ API** for your project:
   - Navigate to "APIs & Services" > "Library".
   - Search for "Google+ API" and enable it.

3. **Create OAuth 2.0 credentials**:
   - Go to "APIs & Services" > "Credentials".
   - Click on "Create Credentials" and select "OAuth client ID".
   - Configure the consent screen and set up your application type (Web application).
   - Add authorized redirect URIs (e.g., `http://localhost:5000/login/callback`).

4. **Get your credentials**:
   - After creating your credentials, you will receive a `CLIENT_ID` and `CLIENT_SECRET`.

5. **Set environment variables**:
   You need to add your credentials to your environment variables. You can do this by creating a `.env` file in your project directory with the following content:
   ```plaintext
   GOOGLE_CLIENT_ID=your_client_id_here
   GOOGLE_CLIENT_SECRET=your_client_secret_here
   ```
   Replace `your_client_id_here` and `your_client_secret_here` with your actual credentials.

## Running the Application
To start the application, run the following command in your terminal:
```bash
python app.py
```
The application will start on `https://localhost:5000`.

## Usage
1. Open your web browser and navigate to `https://localhost:5000`.
2. Click on the "Login" button to authenticate with your Google account.
3. Once logged in, you can access legal consultation information.

## Video Tutorial
If you need assistance setting up your Google OAuth credentials, please watch this helpful video: [Setting Up Google OAuth Credentials](https://youtu.be/tgO_ADSvY1I?si=3BgENI3S0g6tjwjc).
This is how i learnt and be vigilant to hide your `CLIENT_ID` and `CLIENT_SECRET` while pushing your code to Github or anywhere public

##License 
Fell free to fork this code and do as you wish
