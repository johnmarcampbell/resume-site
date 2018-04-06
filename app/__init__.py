from flask import Flask, render_template
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    """Function to create and return an application"""
    app = Flask(__name__)
    bootstrap.init_app(app)

    from .main import main as blueprint
    app.register_blueprint(blueprint)

    return app
