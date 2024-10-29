from flask import Flask, render_template, jsonify

ws = Flask(__name__)

@ws.route('/')
def home():
    return render_template('index.html')

@ws.route('/about')
def about():
    return render_template('about.html')

@ws.route('/api/data', methods = ['GET'])
def get_data():
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    ws.run(debug = True)