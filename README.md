# Webhook Tester

This is a simple Flask application that can be used to test webhooks. It uses ngrok to expose the local server to the internet.

## Prerequisites

- Python 3.7+
- pip
- ngrok

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/wayfaster/webhook-tester.git
   cd webhook-tester
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install ngrok if you haven't already. You can download it from [ngrok.com](https://ngrok.com/download) or use a package manager.

## Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```
   This will start the server on `http://localhost:5000`.

2. In a new terminal window, start ngrok to expose your local server:
   ```
   ngrok http 5000
   ```
   ngrok will provide you with a public URL that forwards to your local server.

3. Use the ngrok URL as your webhook URL when setting up your webhook. For example:
   ```
   https://1234abcd.ngrok.io/wayfaster-webhook
   ```

4. The application will now receive and log any POST requests sent to the `/webhook` endpoint.

## Usage

- The application logs all incoming webhook payloads to the console.
- You can modify the `app.py` file to add custom logic for handling different types of webhook events.

## Note

Remember that ngrok URLs are temporary and will change each time you restart ngrok. For persistent testing, consider using a paid ngrok account or a similar service that provides static URLs.

