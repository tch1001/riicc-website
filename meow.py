from flask import Flask
from flask import render_template, redirect

app = Flask(__name__, static_url_path='/static')

subpages = ['home','projects','news','members','gallery','3dprinting','purchase','contact']

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.route('/<sub>')
def index(sub = None):
	if(sub == None): sub = 'home'
	print(sub)
	return render_template('{}.html'.format(sub))
