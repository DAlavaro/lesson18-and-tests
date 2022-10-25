class Config(object):
    DEBUG = True
    SECRET = 'test'
    API_URL = 'https://jsonkeeper.com/b/GLXT'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}