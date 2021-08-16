from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Pipeline DevOps -> Grupo 8"

if __name__ == '__main__':
    app.run(debug=True)
