#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length

class TodoListForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 64)])
    status = RadioField('done or not', validators=[DataRequired()],  choices=[("1", 'done'),("0",'not yet')])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    username = StringField('user', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('password', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('login')
