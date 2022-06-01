from flask import Blueprint, make_response, jsonify, request
from marshmallow import EXCLUDE
from sqlalchemy import exc
from app import db
from app.models.estacoes import Estacoes, EstacoesSchema


class EstacoesController:
    estacoes_controller = Blueprint(name='estacoes_controller', import_name=__name__)

    @estacoes_controller.route('/estacoes', methods=['GET'])
    def get_estacoes():
        estacoes_list = Estacoes.query.all()
        estacoes_schema = EstacoesSchema(many=True)
        estacoes = estacoes_schema.dump(estacoes_list)
        return make_response(jsonify({
            "estacoes": estacoes
        }))

    @estacoes_controller.route('/estacoes/<id>', methods=['GET'])
    def get_estacao(id):
        estacao = Estacoes.query.filter_by(id_estacao=id).first_or_404()
        estacoes_schema = EstacoesSchema()
        estacao_dumped = estacoes_schema.dump(estacao)
        return make_response(jsonify({
            "estacao": estacao_dumped
        }))

    @estacoes_controller.route('/estacoes', methods=['POST'])
    def create_estacao():
        try:
            data = request.get_json()
            estacoes_schema = EstacoesSchema(unknown=EXCLUDE)
            estacao = estacoes_schema.load(data)

            response = estacoes_schema.dump(estacao.create())
            return make_response(jsonify({
                "estacao": response
            }), 201)

        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409

    @estacoes_controller.route('/estacoes/<id>', methods=['PUT'])
    def update_estacao(id):
        try:
            estacao = Estacoes.query.get(id)
            data = request.get_json()
            estacoes_schema = EstacoesSchema()
            estacao_dumped = estacoes_schema.dump(estacao)
            estacao_dumped.update(data)
            estacao_updated = estacoes_schema.load(estacao_dumped)
            estacao_updated.update()
            return make_response(jsonify({
                "estacao": estacao_dumped
            }), 201)

        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409

    @estacoes_controller.route('/estacoes/<id>', methods=['DELETE'])
    def delete_estacao(id):
        try:
            estacao = Estacoes.query.get(id)
            db.session.delete(estacao)
            db.session.commit()
            return make_response(jsonify({
                "message": "Estacao deleted"
            }), 204)

        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409
