from flask import Flask

app = Flask(__name__);

@app.route("/")
def pagina_inicial():
    return 'teste'

@app.route('/double')
def pagina_double():
    return 'teste2'

