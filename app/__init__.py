from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)

from app.models import estacoes
db.create_all()

from app.controllers.estacoes_controller import EstacoesController
app.register_blueprint(EstacoesController.estacoes_controller, url_prefix='/api/v1/')