from tarefas import *
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
dicionario = globaldict()

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
    if request.method == 'GET':
        return dicionario.dict
    if request.method == 'POST':
        dicionario.add_coisa(request.form['coisa'])
        resp = jsonify(success=True)
        return resp

@app.route('/Tarefa/<id>', methods=['GET', 'PUT', 'DELETE'])
def Tarefa_id(id):
    if request.method == 'GET':
        resp = dicionario.get_coisa(id)
        if (resp != False):
            return resp
        resp = jsonify(success = False)
        return resp
    if request.method == 'PUT':
        resp = dicionario.update_coisa(id, request.form['coisa'])
        resp = jsonify(success=(resp != False))
        return resp
    if request.method == 'DELETE':
        resp = dicionario.deleta_coisa(id)
        resp = jsonify(success=(resp != False))
        return resp

@app.route('/healthcheck')
def healthcheck():
    resp = jsonify(success = True)
    return resp

if __name__ == '__main__':
    app.run()
