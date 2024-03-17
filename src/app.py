from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)


@app.route("/details")
def fetchDetails():
    return {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
    }


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    """This functions executes the flask app and deploys it on localhost:5000"""
    app.run(host="0.0.0.0", port=4000, debug=True)
