from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # Change this to your actual application logic

if __name__ == "__main__":
    app.run(debug=True)  # This runs the app in debug mode
