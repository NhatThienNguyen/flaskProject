from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! :)'


if __name__ == '__main__':
    app.run()

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f"Hello! {name}"

@app.route('/f/<celsius>')
def f(celsius):
    celsius = float(celsius)
    return f"Input Celsius: {celsius}\nFahrenheit: {(celsius * 1.8) + 32}"