from app import app
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'for example...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////' +\
                               os.path.join(basedir, 'model_tmp.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
