from flask import Flask
app = Flask("MyMap")

@app.route("/")
def hello():
    return "Hello World!"
