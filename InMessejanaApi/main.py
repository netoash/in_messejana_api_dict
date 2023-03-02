from flask import Flask, jsonify, request, make_response
from bd import restaurantes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/restaurantes', methods = ['GET'])
def get_restaurantes():
    return make_response(
        jsonify(
                mensagem = 'lista de restaurantes',
                dados = restaurantes
            )
        )

@app.route('/restaurantes/<int:id>',methods=['GET'])
def get_restaurantes_by_id(id):
    for restaurante in restaurantes:
        if restaurante.get('id') == id:
            return make_response(
                jsonify(restaurante)
            )
        
@app.route('/restaurantes', methods = ['POST'])
def cadastrar_retaurante():
    restaurante = request.json
    restaurantes.append(restaurante)
    return make_response(
        jsonify(
            mensagem = 'restaurantecadastrado com sucesso!!',
            restaurante = restaurante
        )
        )

@app.route('/restaurantes/<int:id>',methods=['PUT'])
def edit_restaurantes_by_id(id):
    restaurante_alterado = request.get_json()
    for indice,restaurante in enumerate(restaurantes):
        if restaurante.get('id') == id:
            restaurantes[indice].update(restaurante_alterado)
            return make_response(
                jsonify(restaurantes[indice])
            )

@app.route('/restaurantes/<int:id>',methods=['DELETE'])
def delete_restaurante(id):
    for indice, restaurante in enumerate(restaurantes):
        if restaurante.get('id') == id:
            del restaurantes[indice]

    return make_response(
        jsonify(restaurantes)   
    )

app.run(port = 5000, host = 'localhost', debug = True)