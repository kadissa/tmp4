from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Freddy kruger'}
    posts = [
        {
            'author': {'username': 'Gretta tumberg'},
            'body': ' I like blue whiles'
        },
        {
            'author': {'username': 'Freddy kruger'},
            'body': "I'm coming to you"

        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'''user {form.username.data} entered. remember_me={form.remember_me.data}''')
        return redirect(url_for('index'))
    return render_template('login.html', title='LoginPage', form=form)
