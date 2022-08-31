from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'


@app.route('/say/<string:name>')
def hola(name):
    return f'Hola {name}'

@app.route('/repeat/<int:num>/<string:text>')
def repeat(num,text):
    return (num * text)


if __name__ == '__main__':
    app.run(debug=True)