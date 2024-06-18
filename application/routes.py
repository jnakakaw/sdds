from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/recidivismclassify", methods=['GET', 'POST'])
def recidivismclassify():

    #extract form inputs
    Percent_Days_Employed = request.form.get("Percent_Days_Employed")
    Supervision_Risk_Score_First = request.form.get("Supervision_Risk_Score_First")
    Prior_Arrest_Episodes_PPViolationCharges = request.form.get("Prior_Arrest_Episodes_PPViolationCharges")
    Gang_Affiliated = request.form.get("Gang_Affiliated")
    Prior_Arrest_Episodes_Felony = request.form.get("Prior_Arrest_Episodes_Felony")
    Age_at_Release = request.form.get("Age_at_Release")
    Prior_Arrest_Episodes_Property = request.form.get("Prior_Arrest_Episodes_Property")
    DrugTests_THC_Positive = request.form.get("DrugTests_THC_Positive")
    Prior_Arrest_Episodes_Misd = request.form.get("Prior_Arrest_Episodes_Misd")
    Prior_Conviction_Episodes_Prop = request.form.get("Prior_Conviction_Episodes_Prop")
    Prison_Offense_Violent_Sex = request.form.get("Prison_Offense_Violent_Sex")
    Condition_MH_SA = request.form.get("Condition_MH_SA")
    Prior_Conviction_Episodes_Misd = request.form.get("Prior_Conviction_Episodes_Misd")
    Prison_Years = request.form.get("Prison_Years")

   #convert data to json
    input_data = json.dumps({"Percent_Days_Employed": Percent_Days_Employed, "Supervision_Risk_Score_First": Supervision_Risk_Score_First,
                             "Prior_Arrest_Episodes_PPViolationCharges": Prior_Arrest_Episodes_PPViolationCharges, "Gang_Affiliated": Gang_Affiliated,
                             "Prior_Arrest_Episodes_Felony": Prior_Arrest_Episodes_Felony, "Age_at_Release": Age_at_Release, 
                             "Prior_Arrest_Episodes_Property": Prior_Arrest_Episodes_Property, "DrugTests_THC_Positive": DrugTests_THC_Positive,
                             "Prior_Arrest_Episodes_Misd": Prior_Arrest_Episodes_Misd, "Prior_Conviction_Episodes_Prop": Prior_Conviction_Episodes_Prop,
                             "Prison_Offense_Violent_Sex": Prison_Offense_Violent_Sex, "Condition_MH_SA": Condition_MH_SA, 
                             "Prior_Conviction_Episodes_Misd": Prior_Conviction_Episodes_Misd, "Prison_Years": Prison_Years})

    #url for bank marketing model
    url = "http://localhost:5020/api"
    #url = "https://bank-model-app.herokuapp.com/api"
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", Percent_Days_Employed = Percent_Days_Employed, 
                           Supervision_Risk_Score_First = Supervision_Risk_Score_First, 
                           Prior_Arrest_Episodes_PPViolationCharges = Prior_Arrest_Episodes_PPViolationCharges, 
                           Gang_Affiliated = Gang_Affiliated, Prior_Arrest_Episodes_Felony = Prior_Arrest_Episodes_Felony, Age_at_Release = Age_at_Release, 
                           Prior_Arrest_Episodes_Property = Prior_Arrest_Episodes_Property, DrugTests_THC_Positive = DrugTests_THC_Positive,
                           Prior_Arrest_Episodes_Misd = Prior_Arrest_Episodes_Misd, Prior_Conviction_Episodes_Prop = Prior_Conviction_Episodes_Prop,
                           Prison_Offense_Violent_Sex = Prison_Offense_Violent_Sex, Condition_MH_SA = Condition_MH_SA, 
                           Prior_Conviction_Episodes_Misd = Prior_Conviction_Episodes_Misd, Prison_Years = Prison_Years, 
                           results=results.content.decode('UTF-8'))