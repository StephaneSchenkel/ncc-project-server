import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/poulet', methods=['GET'])
def home():
    return jsonify("test:test")

@app.route('/poulet/<id>', methods=['GET'])
def getFromId(id):
    return jsonify(id +":test")

@app.route('/poulet', methods=['POST'])
def addPoulet():
    content = request.json
    return jsonify("typehas:" + content['type'])

if "__main__" == __name__:
    app.run(host='0.0.0.0', port=8090)