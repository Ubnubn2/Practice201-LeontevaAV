from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevOps!", "status": "ok"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route('/api/users')
def users():
    return jsonify({"users": ["user1", "user2", "user3"]})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
