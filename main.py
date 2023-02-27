from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

@app.route('/exam-tracker')
def exam_tracker():
    return render_template('exam-tracker.html')

@app.route('/daily-quiz')
def daily_quiz():
    return render_template('in-progress.html')

@app.route('/webscraper-tools')
def webscraper():
    return render_template('in-progress.html')

@app.route('/useful-resources')
def resources():
    return render_template('in-progress.html')

