from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    if not user_prompt:
        return jsonify({"error": "Prompt required"}), 400

    try:
        # Add system context to guide the AI
        system_prompt = (
            "You are a helpful and expert AI fitness coach named BodySync. "
            "Always provide workout plans, health advice, and motivational fitness tips. "
            "Answer in a friendly and knowledgeable tone. "
            "User says: "
        )
        full_prompt = system_prompt + user_prompt

        response = model.generate_content(full_prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
