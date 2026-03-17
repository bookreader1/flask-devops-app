from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "DevOps Pipeline Project is Running 🚀"

@app.route('/health')
def health():
    return jsonify(status="OK")

@app.route('/api/data')
def data():
    return jsonify(message="Hello from Flask API", success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)