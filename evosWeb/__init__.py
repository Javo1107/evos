import os

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY']='KEY'


    @app.route('/')
    def index():
        return render_template('welcome.html')
    
    @app.route('/menu')
    def menu():
        return render_template('menu.html')
    
    @app.route('/details')
    def details():
        return render_template('details.html')
    
    @app.route('/orders')
    def orders():
        return render_template('orders.html')
    
    

    return app