from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def health_check():
    return {
        "status": "healthy",
        "service": "dockerized-ci-cd-automation",
        "environment": os.getenv("ENVIRONMENT", "production")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
