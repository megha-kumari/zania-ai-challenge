from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Zania AI Challenge!"

if __name__ == '__main__':
    app.run(debug=True)

