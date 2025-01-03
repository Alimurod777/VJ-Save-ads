from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        return 'Hello from Koyeb'
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
