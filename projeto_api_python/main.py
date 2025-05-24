from flask import Flask, jsonify, request
from bd_alunos import Alunos

app = Flask(__name__)   

@app.route('/Alunos', methods=['GET'])
def get_alunos():
    return jsonify (Alunos)

    

@app.route('/Alunos', methods=['POST'])
def create_novo_aluno():
    novo_aluno = request.get_json()
    Alunos.append(novo_aluno)
    
    return jsonify (novo_aluno)





app.run() 
