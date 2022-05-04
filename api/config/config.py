from decouple import config
from datetime import timedelta

class Config:
    SECRET_KEY = config('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=45)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=45)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:foxtrot09er@localhost/pizza' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:foxtrot09er@localhost/pizza_test' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass

config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}