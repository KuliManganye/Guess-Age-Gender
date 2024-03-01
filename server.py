from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    # Using the Genderize API, A simple API that guesses what gender most likely would be given to a person of a
    # particular name
    genderize_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(genderize_url)
    gender_data = gender_response.json()
    gender_final = gender_data["gender"]

    # Agify API, A simple API that determines the age of a particular name is
    agify_url = f"https://api.agify.io?name={name}"
    agify_response = requests.get(agify_url)
    agify_data = agify_response.json()
    agify_age = agify_data["age"]
    return render_template("guess.html", name=name, gender=gender_final, age=agify_age)

if __name__ == "__main__":
    app.run(debug=True)
