
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
    sex = db.Column(db.String(10), nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    smoker = db.Column(db.String(5), nullable=False)
    region = db.Column(db.String(10), nullable=False)
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

        if sex == 1:
            sex_db = "Male"
        else:
            sex_db = "Female"

        if smoker == 1:
            smoker_db = "Yes"
        else:
            smoker_db = "No"

        if region == 0:
            region_db = "southeast"
        elif region == 1:
            region_db = "southwest"
        elif region == 2:
            region_db = "northeast"
        else:
            region_db = "northwest"

        with open('model.pickle', 'rb') as f:
            mp = pickle.load(f)
        prediction_val = round(float(mp.predict(inputs)),4)
        data = Predictions(age=age, sex=sex_db, bmi=bmi, children=children, smoker=smoker_db, region=region_db, pred=prediction_val)
        db.session.add(data)
        db.session.commit()
    return render_template('index.html', prediction_text="Your insurace premium will be $", prediction_val=prediction_val)

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