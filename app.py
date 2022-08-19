
from lib2to3.pgen2.grammar import opmap_raw
import re
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = 'super-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///predictions.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Predictions(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    smoker = db.Column(db.Integer, nullable=False)
    region = db.Column(db.Integer, nullable=False)
    pred = db.Column(db.Float, nullable = True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    db.create_all()

    def __repr__(self) -> str:
        return f"{self.sno} - {self.age} - {self.sex} - {self.bmi} - {self.children} - {self.smoker} - {self.region} - {self.pred}"

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def model():
    if request.method=='POST':
        age = request.form['age']
        sex = request.form['sex']
        bmi = request.form['bmi']
        children = request.form['children']
        smoker = request.form['smoker']
        region = request.form['region']
        inputs = np.array([[age, sex, bmi, children, smoker, region]])

        with open('model.pickle', 'rb') as f:
            mp = pickle.load(f)
        prediction_val = round(float(mp.predict(inputs)),4)
        data = Predictions(age=age, sex=sex, bmi=bmi, children=children, smoker=smoker, region=region, pred=prediction_val)
        db.session.add(data)
        db.session.commit()
    return render_template('index.html', prediction_text="Your insurace premium will be", prediction_val=prediction_val)

@app.route('/bmi_cal', methods=['GET','POST'])
def bmi_cal():
    if request.method=='POST':
        age = request.form['age']
        height = request.form['height']

    bmi = age/height**2
    return render_template('index.html',bmi=bmi)

@app.route('/predictions', methods=['GET','POST'])
def predictions():
    allpreds = Predictions.query.all() 
    return render_template('predictions.html',allpreds=allpreds)

@app.route('/analysis', methods=['GET','POST'])
def analysis():
    return render_template('analysis.html')

@app.route('/delete/<int:sno>')
def delete(sno):
    data = Predictions.query.filter_by(sno=sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect("/predictions")


if __name__ == "__main__":
    app.run(debug=True, port=5000)