from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps -> Grupo 8"

if __name__ == '__main__':
   app.run(debug=True)
