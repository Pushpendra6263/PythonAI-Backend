# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import openai
# import os

# app = Flask(__name__)
# CORS(app, origins="http://localhost:3000")

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_message = data.get('message')
#     api_key = data.get("apiKey") or os.getenv("OPENAI_API_KEY")  # Use API key from request or .env
#     print(user_message , api_key)
#     if not user_message:
#         return jsonify({"response": "Message is required."}), 400

#     if not api_key:
#         return jsonify({"response": "API key is missing."}), 400

#     openai.api_key = api_key  # Set OpenAI API key

#     try:
#         response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # Updated model
#         messages=[
#             {"role": "system", "content": "You are a friendly AI tutor named PythonPal. Teach basic Python concepts to children in a simple and engaging way."},
#             {"role": "user", "content": user_message}
#         ]
# )

#         return jsonify({"response": response['choices'][0]['message']['content']}), 200

#     except openai.error.OpenAIError as e:  # Catch OpenAI API errors
#         return jsonify({"response": f"OpenAI API error: {str(e)}"}), 500

#     except Exception as e:  # Catch general errors
#         return jsonify({"response": f"An unexpected error occurred: {str(e)}"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

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
    app.run(debug=True)







