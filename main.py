from requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "845ec3fb6210c0055287e6bdcc07eae4"
url = ('https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}&lang=pt_br'))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
