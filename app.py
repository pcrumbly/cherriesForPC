from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

cherries = 0
cherries_file = 'cherries.json'

if not os.path.exists(cherries_file):
    with open(cherries_file, 'w') as f:
        json.dump({"cherries": cherries}, f)


@app.route('/cherries', methods=['GET', 'POST'])
def handle_cherries():
    global cherries

    if request.method == 'GET':
        return jsonify({"cherries": str(cherries)})

    elif request.method == 'POST':
        data = request.json
        increment_amount = data.get('increment', 1)  # Get the increment amount (default to 0)
        cherries += increment_amount  # Increment cherries value

        with open(cherries_file, 'w') as f:
            json.dump({"cherries": cherries}, f)

        return jsonify({"cherries": str(cherries)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
