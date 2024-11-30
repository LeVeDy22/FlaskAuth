from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields import StringField, SubmitField
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=20)]
    )
    password = StringField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = StringField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
