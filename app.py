from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("ExamKnearestneighborclassifier.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result


@app.route("/")
def index():
    return render_template("index.html");
@app.route('/result',  methods =["GET", "POST"])
def result():
    if request.method == "POST":

       age = request.form.get("age")
       # getting input with name = lname in HTML form
       Glucose = request.form.get("Glucose")
       bp= request.form.get("bp")
       skinthickness= request.form.get("skinthickness")
       insulin = request.form.get("insulin")
       bmi = request.form.get("bmi")
       Gender = request.form.get("Gender")
       pedigreefunction = request.form.get("pedigreefunction")

       l1=[age,Glucose,bp,skinthickness,insulin,bmi,Gender,pedigreefunction]
       answer = ValuePredictor(l1)
    return render_template("result.html",Age=answer)


if __name__ == '__main__':
   app.run(debug = True)
