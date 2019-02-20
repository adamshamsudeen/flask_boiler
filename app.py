from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html',title="Home")

@app.route('/animals')
def page():
	animals = ['cat', 'cow', 'horse', 'dog']
	lucky_animal = random.choice(animals)
	return render_template('animals.html',
					animals = animals,
					title = "Animals",
					lucky_animal = lucky_animal)


if __name__ == '__main__':
	app.run(debug=True)
