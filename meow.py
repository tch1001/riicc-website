from flask import Flask
from flask import render_template, redirect

app = Flask(__name__, static_url_path='/static')

subpages = ['home','projects','news','members','gallery','3dprinting','purchase','contact']

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.route('/')
@app.route('/<sub>')
def index(sub = None):
	if(sub == None): sub = 'home'
	print(sub)
	return render_template('{}.html'.format(sub))
@app.route('/purchase/submit', methods=['POST'])
def submitPurchase():
	form = PurchaseForm()
	assert(request.method=='POST')
	if(form.validate() == False):
		flash("All fields are required.")
		return render_template('purchase.html',form=form)
	else: return render_template("purchase_success.html")
