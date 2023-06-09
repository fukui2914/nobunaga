from flask import Flask, render_template, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data['message']

    messages = [
        {
            "role": "system", 
            "content": """
            以降のチャットにおいてあなたは下記の制約条件を厳密に守ってください。
            制約条件
            *歴史人物の織田信長のchatbotとしてロールプレイを行ってください。
            *あなたは織田信長です。
            *織田信長の口調は、「〜じゃ」「〜だ」「〜である」などの口調を好みます。
            *織田信長は「〜です」「〜ます」などの口調は絶対に用いません。 
            *織田信長は常に二文程度の非常に短い文章で回答します。
            """
        },
        {"role": "user", "content": user_message},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    gpt_response = response.choices[0].message['content'].strip()

    return jsonify({'message': gpt_response})

if __name__ == "__main__":
    app.run(debug=True)


