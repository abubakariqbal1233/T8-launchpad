import os
from flask import Flask

app = Flask(__name__)

# Load configs from System Environment (Default to 'dev' and port 4000)
ENVIRONMENT = os.getenv("APP_ENV", "dev")
PORT = int(os.getenv("APP_PORT", 4000))

@app.route("/")
def home():
    # Logic to differentiate between environments
    if ENVIRONMENT == "live":
        return "Welcome to Live - VERSION 2.0 (Automated!)"
    return "Welcome to Dev"

if __name__ == "__main__":
    # Host="0.0.0.0" allows the app to be accessible via the EC2 Public IP
    app.run(host="0.0.0.0", port=PORT)