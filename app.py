import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/ask_assistant', methods=['POST'])
def ask_assistant():
    user_input = request.json['user_input']
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_response = response['choices'][0]['message']['content']
    return jsonify({"response": assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
