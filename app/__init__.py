# importing Flask class from flask.py file
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# create an instance of the Flash class, in order to run this application
# name parameter will default to folder name
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

# you have to instatiate the database variables after the config has been set
# reason is that the config holds the location of the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# from the app folder, import the routes.py file, and startup at the index route
from app import routes
