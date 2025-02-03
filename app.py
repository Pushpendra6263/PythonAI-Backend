from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
# CORS(app, origins="https://pythonai.netlify.app/")
CORS(app)

@app.route('/')
def home():
    return "Flask server is running successfully!"

# Set Gemini API Key from request or .env file
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    api_key = data.get("apiKey") or os.getenv("GEMINI_API_KEY")  # Use API key from request or environment

    if not user_message:
        return jsonify({"response": "Message is required."}), 400

    if not api_key:
        return jsonify({"response": "API key is missing."}), 400

    # Configure Gemini API Key
    genai.configure(api_key=api_key)

    try:
        # Initialize Gemini model
        model = genai.GenerativeModel("gemini-pro")
        
        # Generate response
        response = model.generate_content(user_message)
        
        return jsonify({"response": response.text}), 200

    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # app.run(debug=True)
    port = 5000
    app.run(host="0.0.0.0", port=port, debug=True)







