from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
#https://stackoverflow.com/questions/25324113/email-validation-from-wtform-using-flask

class UsersForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()]) 
	last_name = StringField('Last Name', validators=[DataRequired()]) 
	age = IntegerField('Age', validators=[DataRequired()])
	email = EmailField('Email address', validators=[DataRequired(), Email()])
	submit = SubmitField('Enter')

class DeleteUserForm(FlaskForm):
	submit = SubmitField('delete')