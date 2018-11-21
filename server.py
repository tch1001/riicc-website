from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

subpages = ['home','projects','news','members','gallery','3dprinting','purchase','contact']

@app.route('/')
@app.route('/<sub>')
def index(sub = None):
	if(sub == None): sub = 'home'
	if(sub in subpages): return render_template('{}.html'.format(sub))
	else: return render_template('404.html')
