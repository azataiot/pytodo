#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length

class TodoListForm(FlaskForm):
    title = StringField('Атауы', validators=[DataRequired(), Length(1, 64)])
    status = RadioField('Аяқталды', validators=[DataRequired()],  choices=[("1", 'Мүмкін'),("0",'Жоқ')])
    submit = SubmitField('Жіберу')


class LoginForm(FlaskForm):
    username = StringField('Пайдаланушы аты', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('Құпия сөз', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('Кіру')
