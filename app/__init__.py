import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # .env file से variables लोड करें

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load SECRET_KEY
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "defaultsecret")

    # Load MySQL URL — with pymysql
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://pankaj123:Pankaj%40123@localhost:3306/users"
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app
