# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = "postgres://yuwopqkgrjamhk:53ce3763ed92be24b9e889000552a5a54cbc48b107652a09038173d51ac59326@ec2-3-219-135-162.compute-1.amazonaws.com:5432/dabuqj9aebubsl"
    # '{}://{}:{}@{}:{}/{}'.format(
    #     os.getenv('DB_ENGINE'   , 'mysql+pymysql'),
    #     os.getenv('DB_USERNAME' , 'ec2-3-219-135-162.compute-1.amazonaws.com'),
    #     os.getenv('DB_PASS'     , 'dabuqj9aebubsl'),
    #     os.getenv('DB_HOST'     , 'yuwopqkgrjamhk'),
    #     os.getenv('DB_PORT'     , 5432),
    #     os.getenv('DB_NAME'     , '53ce3763ed92be24b9e889000552a5a54cbc48b107652a09038173d51ac59326')
    # )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
