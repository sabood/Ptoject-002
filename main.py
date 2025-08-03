from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Saboods World!'

app.run(port=5000, debug=True)  