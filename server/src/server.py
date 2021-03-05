from flask import Flask
from flask import Response, request, redirect, render_template
import requests


app = Flask(__name__)

# dictionary to act as local cache storing all sites visited in a single instance of the program






@app.route('/')
def index():
    render_template('home.html')
    

@app.route('/Personal',methods=['GET'])
def proxy():
    render_template('home.html')
    
    


if __name__ == '__main__':
    app.run(debug = False,port=5000)

    