#import app variable instance in order to run application
# also import necessary flask methods
from app import app
from flask import render_template, url_for, redirect


# create route for index page, render index.html file
@app.route('/')
@app.route('/index')
def index():
    # takes as many args as needed, first arg is index.html, rest are in the
    # information you want to pass in to render in index.html

    name = 'Jon Snow'
    # characters = ['Arya', 'Jamie', 'Jon', 'Ned', 'Daenarys', 'Tyrion']

    characters = {
        'females': ['Arya', 'Daenarys'],
        'males': ['Jaimie', 'Jon', 'Ned','Tyrion']
    }

    return render_template('index.html', name=name, characters=characters)


@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/elsewhere')
def go_elsewhere():
    return redirect(url_for('index'))

@app.route('/profile/<name>/<gender>', methods=['GET'])
def profile(name, gender):
    info = {}
    if name == 'Arya':
        info = {
            'prof_pic': 'http://placehold.it/250x250',
            'house': 'Stark',
            'home': 'Winterfell',
            'weapon': 'Needle'
        }
    elif name == 'Jaimie':
        info = {
            'prof_pic': 'http://placehold.it/250x250',
            'house': 'Lannister',
            'home': 'Castille Rock',
            'weapon': 'Bastard sword'

        }
    return render_template('profile.html', name=name, info=info, gender=gender)
