from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv("AIzaSyACDMEbRnQcHRiF9w7fV2OfqEl3XnTCZ6A"))

model = genai.GenerativeModel('gemini-pro')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt required"}), 400

    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
