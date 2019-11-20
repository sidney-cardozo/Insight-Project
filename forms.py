from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

