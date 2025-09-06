from flask import Flask, request, jsonify
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests, json

app = Flask(__name__)

# Load service account key
creds = service_account.Credentials.from_service_account_file(
    "dialogflow-key.json",
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
