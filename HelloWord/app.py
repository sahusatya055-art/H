from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is my first Flask app 🚀"

if __name__ == '__main__':
    # Run the app on http://127.0.0.1:5000
    app.run(debug=True)


