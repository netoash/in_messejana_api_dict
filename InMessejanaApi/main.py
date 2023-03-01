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
app.run(port = 5000, host = 'localhost', debug = True)