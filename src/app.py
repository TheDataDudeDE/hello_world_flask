# app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<H1>Hello, World from Azure! Reloaded</H1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
