from flask import Flask, render_template
from routes.index import routers
from routes.api import apis
from routes.consommation_api import consommation

from routes.visualisation import visualisations
from flask_sqlalchemy import SQLAlchemy
from models.create_tables import create_all_tables

from flask_cors import CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = 'groupe3'
# CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/projet_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}}) 



#Pour gerer les routes
app.register_blueprint(routers)
app.register_blueprint(apis)
app.register_blueprint(visualisations)
app.register_blueprint(consommation)



#Pour la page 404
@app.errorhandler(404)
def not_found(error):
    return render_template('pages/not_found.html'),404



if __name__=='__main__':
    create_all_tables()
    app.run(debug=True,port=5000)