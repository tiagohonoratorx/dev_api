from flask_restful import Resource

lista_habilidades = ['Python', 'PHP', 'Java', 'CSS', 'Flask']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

