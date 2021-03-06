from flask import Flask
from flask import Response, request, redirect, render_template

import requests


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('home.html')

@app.route('/Personal')
def proxy():
    return render_template('home.html')
    
    


if __name__ == '__main__':
    app.run(debug = False,port=5000)

    