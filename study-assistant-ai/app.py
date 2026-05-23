from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables
load_dotenv()

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    try:

        completion = client.chat.completions.create(

           model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]

        )

        ai_response = completion.choices[0].message.content

        return jsonify({
            "response": ai_response
        })

    except Exception as e:

        return jsonify({
            "response": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)