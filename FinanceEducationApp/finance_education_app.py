
from flask import Flask, session, redirect, url_for, escape, request, Response, abort
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from flask_wtf import FlaskForm, FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import json
from datetime import date
import numpy as np
import pandas as pd
import datetime
import math
import sys
from FinanceEducationApp import db

# init SQLAlchemy so we can use it later in our models
#db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

print (sys.path)

from FinanceEducationApp.models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# blueprint for auth routes in our app
from FinanceEducationApp.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from FinanceEducationApp.main import main as main_blueprint
app.register_blueprint(main_blueprint)

