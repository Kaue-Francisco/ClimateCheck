import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def consulta(city):
    API_KEY = "845ec3fb6210c0055287e6bdcc07eae4"
    url = (f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}&lang=pt_br')
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/resposta', methods=['POST', 'GET'])
def resposta():
    if request.method == 'POST':
        city = request.form['city']
        r = consulta(city)
        if r['cod'] == "400":
            return render_template('index.html', aviso="Não foi encontrado essa cidade!")
        else:
            city = r['name']
            temp = r['main']['temp']
            description = r['weather'][0]['description']
            return render_template('resposta.html', city=city, temp=round(temp), description=description)    

    else:
        return render_template('resposta.html')

if __name__ == "__main__":
    app.run(debug=True)
