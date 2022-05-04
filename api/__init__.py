from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from .models.orders import Order
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed


def create_app(config = config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)

    #this acts like blueprint with the syntax being
    #api.add_namespace(x_namespace, path = '/auth')
    #but if we don't give path it takes it as namespace name
    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace)


    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    @api.errorhandler(NotFound)
    def not_found(error):
        return {'error': 'Not Found'}, 404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {'error': 'Method Not Allowed'}, 405

    

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Order': Order
        }

    return app