from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Travel Search Bot V2!"

@app.route("/search")
def search():
    return jsonify({"message": "Travel search endpoint (to be implemented)"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
