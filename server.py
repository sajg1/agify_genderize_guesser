from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guess_name/<some_name>')
def guess_name(some_name):
    return render_template('guess_name.html', name=some_name)

if __name__ == "__main__":
    app.run(debug=True)