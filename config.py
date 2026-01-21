import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    sqlalchemy_database_uri = os.environ.get('DATABASE_URL') or 'sqlite:///techtrend.db'
    if sqlalchemy_database_uri.startswith("postgres://"):
        sqlalchemy_database_uri = sqlalchemy_database_uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = sqlalchemy_database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERPER_API_KEY = os.environ.get('SERPER_API_KEY')
