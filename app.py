from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id': 2,
        'titulo': 'Harry Potter',   
        'autor': 'J.K. Rowling'
    },
    {
        'id': 3,    
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry'
    },
]

#consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar (id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            if livro.get('id') == id:
                livros[indice].update(livro_alterado)
                return jsonify(livros[indice])
            
#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
        return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
