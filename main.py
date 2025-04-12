from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return "Missing URL", 400

    res = requests.get(url)
    return res.content, res.status_code, {"Content-Type": res.headers.get("Content-Type", "text/html")}

app.run(host="0.0.0.0", port=8080)
