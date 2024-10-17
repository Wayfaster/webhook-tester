from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wayfaster-webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook payload:")
    print(data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
