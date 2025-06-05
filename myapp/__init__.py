from flask import Flask
from app.routes.diet import diet_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(diet_bp, url_prefix='/diet')
    return app
