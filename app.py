import os

from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET',
                                'Please_dont_use_this_default')

class IDForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    age = IntegerField('Age',
                       validators=[validators.NumberRange(0, 100,
                                                          "We expect a number")])
    submit = SubmitField('Submit')

@app.route('/', methods= ['GET', 'POST'])
def index():
    
    form = IDForm()

    if request.method == 'POST' and form.validate():
        return render_template('summary.html',
                               name=request.form['name'],
                               year1 = 2019-int(request.form['age']),
                               year2 = 2020-int(request.form['age']))
    
    else:
        return render_template('form.html', form=form)
                                    

