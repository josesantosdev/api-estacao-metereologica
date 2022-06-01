from sqlalchemy import Column, BigInteger, String, Numeric, CheckConstraint, Integer, DateTime
from app import db, ma


class Estacoes(db.Model):

    __tablename__ = 'Estacoes'

    id_estacao = Column(BigInteger, primary_key=True)
    nome_estacao = Column(String(128), nullable=False)
    cod_regiao = Column(String(2), nullable=False)
    uf = Column(String(2), nullable=False)
    codigo_wmo = Column(String(128), nullable=False)
    latitude = Column(Numeric(), nullable=False)
    longitude = Column(Numeric(), nullable=False)
    altitude = Column(Integer, nullable=False)
    data_fundacao = Column(DateTime, nullable=False)



    def __init__(self, nome_estacao, cod_regiao, uf, codigo_wmo, latitude, longitude, altitude, data_fundacao) -> None:
        self.nome_estacao = nome_estacao
        self.cod_regiao = cod_regiao
        self.uf = uf
        self.codigo_wmo = codigo_wmo
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.data_fundacao = data_fundacao

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Estacaoes: {self.nome_estacao}'

class EstacoesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Estacoes
        sqla_session = db.session
        load_instance = True

    id_estacao = ma.auto_field()
    nome_estacao = ma.auto_field()
    cod_regiao = ma.auto_field()
    uf = ma.auto_field()
    codigo_wmo = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    altitude = ma.auto_field()
    data_fundacao = ma.auto_field()
