from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'op'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': '123'
        },
        {
            'author': {'username': 'Susan'},
            'body': '1234'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)