from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# construir as funcionalidades


@app.route('/')
def homepage():
    return 'A api está no ar'


@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


# rodas a nossa api
app.run(host='0.0.0.0')
