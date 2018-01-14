from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Here's the main page. <a href='http://localhost:5000/seeform'>Click here to see the form</a>."

@app.route('/seeform',methods=["GET","POST"])
def see_form():
    formstring = """<br><br>
    <form action="" method='POST'>
<input type="text" name="phrase"> Enter a phrase: <br>
<input type="submit" value="Submit">
"""
    if request.method == "POST":
    	entered = request.form.get('phrase',"")
    	return "The last phrase entered was {}".format(entered)
    	+ formstring
    else:
        return formstring




if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
