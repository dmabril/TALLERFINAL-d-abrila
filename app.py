from flask import Flask, jsonify, render_template
from models.perro import Perro
from models.gato import Gato
from models.huron import Huron
from models.boa_constrictor import Boa_constrictor

app = Flask(__name__, template_folder="views")


@app.route("/")
def index():
    return render_template("index.html")

#PERRO
@app.route('/perro')
def perro():
    perro = Perro()
    sonido_perro = perro.hacer_sonido()  
    return render_template('perro.html', sonido=sonido_perro)


@app.route('/api/perro/sonido', methods=['GET'])
def get_perro_sonido():
    perro = Perro()
    sonido_perro = perro.hacer_sonido()  
    return jsonify({'sonido_perro': sonido_perro})


#GATO
@app.route('/gato')
def gato():
    gato = Gato()
    sonido_gato = gato.hacer_sonido()  
    return render_template('gato.html', sonido=sonido_gato)


@app.route('/api/gato/sonido', methods=['GET'])
def get_gato_sonido():
    gato = Gato()
    sonido_gato = gato.hacer_sonido()  
    return jsonify({'sonido_gato': sonido_gato})


#HURON
@app.route('/huron')
def huron():
    huron = Huron()
    sonido_huron = huron.hacer_sonido()  
    return render_template('huron.html', sonido=sonido_huron)


@app.route('/api/huron/sonido', methods=['GET'])
def get_huron_sonido():
    huron = Huron()
    sonido_huron = huron.hacer_sonido()  
    return jsonify({'sonido_huron': sonido_huron})


#BOA
@app.route('/boa')
def boa():
    boa = Boa_constrictor()
    sonido_boa = boa.hacer_sonido()  
    return render_template('boa.html', sonido=sonido_boa)


@app.route('/api/boa/sonido', methods=['GET'])
def get_boa_sonido():
    boa = Boa_constrictor()
    sonido_boa = boa.hacer_sonido()  
    return jsonify({'sonido_boa': sonido_boa})


if __name__ == "__main__":
    app.run(debug=True)
