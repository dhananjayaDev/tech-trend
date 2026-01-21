# TechTrend Tracker

A production-ready Flask web application that tracks the latest technology news and trends using the Serper.dev Google Search API. Features secure User Authentication with mandatory Two-Factor Authentication (TOTP).

## Features

- **User Authentication**: Secure registration and login with bcrypt password hashing.
- **Two-Factor Authentication (2FA)**: Mandatory TOTP verification using Google Authenticator / Authy.
- **News Dashboard**: Real-time tech news aggregation with search functionality.
- **Modern UI**: Fully responsive design using Tailwind CSS (Dark/Light mode supported).
- **Secure**: CSRF protection, Session management, Secure password storage.

## Prerequisites

- Python 3.8+
- [Serper.dev](https://serper.dev/) API Key

## Setup Instructions

1.  **Clone or Download the Project**

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    - Rename `.env.example` to `.env`.
    - Open `.env` and add your `SERPER_API_KEY`.
    - (Optional) Update `SECRET_KEY` and `DATABASE_URL`.

5.  **Initialize the Database**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6.  **Run the Application**
    ```bash
    flask run
    ```
    Access the app at `http://127.0.0.1:5000`.

## Usage Guide

1.  **Register**: Create a new account. You will be prompted to scan a QR code.
2.  **Setup 2FA**: Use an authenticator app (e.g., Google Authenticator) to scan the QR code. Enter the 6-digit code to verify.
3.  **Login**: Enter email/username and password. Then enter the OTP from your app.
4.  **Dashboard**: Browse latest tech news or use the search bar for specific topics.
5.  **Profile**: Manage your account or reset 2FA if needed.

## Project Structure

- `app.py`: Main application factory and route definitions.
- `models.py`: Database models (User).
- `forms.py`: Flask-WTF forms.
- `utils.py`: Helper functions for TOTP and QR generation.
- `config.py`: Configuration settings.
- `templates/`: HTML templates (Tailwind CSS).
- `static/`: Static assets (JS/CSS).

## License

MIT
