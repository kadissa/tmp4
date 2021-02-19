from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(message='это поле не должно быть пустым'),
                                       Length(min=5, message='не менее 5 знаков')])
    password = PasswordField(validators=[DataRequired(), Length(min=5, message='не менее 5 знаков')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
