#for flask application. now unused
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def add_numbers(x, y):
    return x + y

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = add_numbers(data['num1'], data['num2'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
