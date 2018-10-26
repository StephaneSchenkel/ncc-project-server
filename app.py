import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return jsonify("test:test")

if "__main__" == __name__:
    app.run(host='0.0.0.0')