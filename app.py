from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		student = request.form['student']
		print(student)
		if student == '':
			return render_template('index.html')
		return render_template('success.html')
	

if __name__ == '__main__':
	app.debug = True
	app.run()
