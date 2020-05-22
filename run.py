from flask import Flask, jsonify
from random import randint
from flask_cors import CORS
from requests import get

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/random', methods=['GET', 'POST'])
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return get('http://localhost:5000/{}'.format(path)).text
    return 'You want the path: %s' % path

if __name__ == '__main__':
    app.run()
