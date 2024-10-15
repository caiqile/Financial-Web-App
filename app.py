from flask import Flask,render_template,request
import google.generativeai as genai
import random
import os
from textblob import TextBlob

api = os.getenv("MAKERSUITE_API_TOKEN") 
# api = "AIzaSyAF_pGbsDW3ccFzWoj4zE1ksnbUIZf0W6w"
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA",methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    q += " Please limit response to 4-5 sentences"
    r = model.generate_content(q)
    return(render_template("makersuite.html",r=r.text))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke", methods=["GET","POST"])
def joke():
    heads = random.randint(0,1)
    if heads:
        r=model.generate_content("Tell me a Singaporean Joke")
    elif not heads:
        r= model.generate_content("Singapore financial news in paragraph form, 2 sentences")
    return render_template("index.html", joke=r.text)

@app.route("/TM", methods=["GET", "POST"])
def TM():
    return(render_template("TM.html"))

@app.route("/SA", methods=["GET", "POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SAR", methods=["GET", "POST"])
def SAR():
    q = request.form.get("q")
    r = TextBlob(q).sentiment
    return(render_template("SAR.html", r=r))

if __name__ == "__main__":
    app.run()
