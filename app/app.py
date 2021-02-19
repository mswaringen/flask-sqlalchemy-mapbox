# app.py
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class School(db.Model):
    __tablename__ = 'schools-geocoded'
    __table_args__ = { 'extend_existing': True }
    LOC_CODE = db.Column(db.Text, primary_key=True) 

@app.route("/")
def hello():
    return render_template("index.html",count=90)

@app.route("/shoelaces")
def shoelaces():
    return "This works now!"

@app.route("/about")
def about():
    return "This is about me"

if __name__ == '__main__':
    app.run(debug=True)
