from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guess/<some_name>')
def guess_name(some_name):
    age_response = requests.get(url=f'https://api.agify.io?name={some_name}')
    gender_response = requests.get(url=f'https://api.genderize.io?name={some_name}')
    guessed_age = age_response.json()['age']
    guessed_gender = gender_response.json()['gender']
    return render_template('guess_name.html', name=some_name, age=guessed_age, gender=guessed_gender)


if __name__ == "__main__":
    app.run(debug=True)