import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eaf2b29a66444de11bb49ebad5dd14e2' #prevent modify cookie
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #'login' is a function in route
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_POST'] = 587
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kungkter21@gmail.com'
app.config['MAIL_PASSWORD'] = 'jkfokxqasnipguqa'
mail = Mail(app)

from flaskblog import routes