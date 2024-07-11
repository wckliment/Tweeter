from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class TweetForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    tweet = TextAreaField('Tweet', validators=[DataRequired()])
    submit = SubmitField('Create Tweet')
