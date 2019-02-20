from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html',title="Home")

@app.route('/animals')
def page():
	animals = ['cat', 'cow', 'horse', 'dog']
	title = {'user_name':'adam'}
	return render_template('animals.html',animals=animals, title="Animals")


if __name__ == '__main__':
	app.run(debug=True)
