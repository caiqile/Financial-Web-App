from flask import Flask,render_template,request
import google.generativeai as palm
import random
import os

api = os.getenv("MAKERSUITE_API_TOKEN") 
# api = "AIzaSyAF_pGbsDW3ccFzWoj4zE1ksnbUIZf0W6w"
palm.configure(api_key=api)
model = {"model": "models/text-bison-001"}

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
    r = palm.generate_text(prompt=q, **model)
    return(render_template("makersuite.html",r=r.result))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke", methods=["GET","POST"])
def joke():
    heads = random.randint(0,1)
    if heads:
        r=palm.generate_text(prompt="Tell me a Singaporean Joke", **model)
    elif not heads:
        r= palm.generate_text(prompt="Singapore financial news in paragraph form, 2 sentences", **model)
    return render_template("index.html", joke=r.result)

if __name__ == "__main__":
    app.run()
