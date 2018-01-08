# Import statements necessary
from flask import Flask
import requests
import json

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def another_function():
    return '<b>Hello World!</b>'

@app.route('/user/<yourname>')
def hello_name(yourname):
    return '<h1>Hello {}</h1>'.format(yourname)

# new route: /itunes/<artist>
@app.route('/itunes/<artist>')
def get_artist_data(artsit):
	# use artist to make req to itunes 
	# get the response 
	# get the data out of the response 
	# manage the data so I pull a list of 
	# strings out of the nested data 
	# return it (with any specific html I want, I guess)
	return string_of_titles

if __name__ == '__main__':
    app.run()
