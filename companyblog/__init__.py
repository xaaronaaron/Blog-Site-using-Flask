import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()

login_manager.init_app(app) #initialize app
login_manager.login_view = 'users.login' #default page to go to

from companyblog.core.views import core
app.register_blueprint(core)# essentially telling your Flask application to include 
                            # and use the routes and views defined within the 'core' Blueprint

from companyblog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

from companyblog.users.views import user_blueprint
app.register_blueprint(user_blueprint)

from companyblog.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)