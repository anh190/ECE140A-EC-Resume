from flask import Flask
from flask import Response, request, redirect, render_template

import requests


app = Flask(__name__)


@app.route('/')
def personal():
    return render_template('home.html')

@app.route('/Resume')
def resume():
    return render_template('resume.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/git_repo')
def toggle():
    resp = requests.get("https://github.com/Toggle-development/TogDev2.0")
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response
    


if __name__ == '__main__':
    app.run(debug = True,port=5000)

    