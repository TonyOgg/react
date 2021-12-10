from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from api.ApiHandler import ApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.debug = True
CORS(app)
api = Api(app)


@app.route("/", defaults={'path':''})
def start_page(path):
    return "rer"


api.add_resource(ApiHandler, '/tests/reports')

if __name__ == "__main__":
    app.run()