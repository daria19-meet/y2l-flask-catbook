from flask import Flask
from flask import render_template
from database import get_all_cats, get_by_name

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/profile/<string:name>')
def profile_page(name):
	cat=get_by_name(name)
	return render_template("cat.html", cat=cat)

@app.route('/add_cat')
def add_cat():
	return render_template("add_cat.html")

if __name__ == '__main__':
   app.run(debug = True)
