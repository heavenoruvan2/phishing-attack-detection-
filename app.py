from flask import Flask,render_template,request
import joblib
from feature_extraction import extract
app=Flask(__name__)
model=joblib.load("phishing_model.pkl")
@app.route("/",methods=["GET","POST"])
def home():
 p=None
 if request.method=="POST":
  r=model.predict([extract(request.form["url"])])[0]
  p="⚠️ Phishing Website" if r else "✅ Safe Website"
 return render_template("index.html",prediction=p)
app.run(debug=True)
