# app.py
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/shoelaces")
def shoelaces():
    return "This works now!"

@app.route("/about")
def about():
    return "This is about me"

if __name__ == '__main__':
    app.run(debug=True)
