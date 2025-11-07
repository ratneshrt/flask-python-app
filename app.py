from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    return "<h1>Hi You are successfully logged in.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)