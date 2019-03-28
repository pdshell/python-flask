import os

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACH_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@192.168.0.137:3306/test?charset=utf8'
