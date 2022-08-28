# Insurance Prediction Webapp

**Webapp**   [Click me.](https://insurancepredictorjitendra.herokuapp.com/)

![Insurance-demo](https://user-images.githubusercontent.com/86119527/187073221-4074a20e-56e9-495b-9ca1-a72505b815d8.gif)

## About this project

An insurance premium is the amount of money an individual or business pays for an insurance policy. Insurance premiums are paid for policies that cover healthcare, auto, home, and life insurance.

This project is focuses on predicting insurance premium using best regression model. The framework is created using *Flask* and deployed on *Heroku*

## Libraries used in this project

- numpy, pandas, matplotlib, seaborn, sklearn

**Data set Available at:** [Click here](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction)

**Data Set Information:**

- Dataset contains 1338 observations (rows) and 7 features (columns). The dataset contains 4 numerical features (age, bmi, children and expenses) and 3 nominal
- features (sex, smoker and region) that were converted into factors with numerical value designated for each level.

**Attributes**

*Numeric attributes*
- **Age:** Person's age *Int*
- **BMI:** BMI of the person *Float*
- **Children:** Number of children *Int*
- **Expenses:** Insurance premium of person *Float*

*Categorical attributes*
- **Sex:** Gender of the person *Nominal*
- **Smoker:** Person is smoker or not? *Nominal*
- **Region:** Region of the person *Nominal*

## Steps

1. Data Collection
2. Data Pre-Processing
3. Exploratory Data Analysis
4. Model Building
5. Model Selection
6. Flask framework
7. Model deployment on heroku 

## Model Building

*Regression* 

- For regression analysis *Expenses(numeric)* considered as dependent feature.

*Model Used:* 

1. Multiple linear regression
2. Decision tree regression
3. Random forest regression

## Model Selection


- For Regression *r2_score* metrics is used to select best model.

- The best *r2_score* Accuracy Model is used for Model Deployment.

## Model Deployment

**Flask**
- Front-end is created using bootstrap-5, Flask and flask-sqlalchemy is used for back-end.

**Heroku**

- Model deployed on *Heroku*.
