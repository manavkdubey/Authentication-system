from flask import Flask, redirect, render_template, request, url_for

import json

def login(username, password):
    # Load the user data from the JSON file
    with open('static\cred.json', 'r') as f:
        data = json.load(f)

    # Check if the username and password match
    for user in data['users']:
        if user['username'] == username and user['password'] == password:
            # Login successful
            return True
    
    # Login failed
    return False


app = Flask(__name__)
app.config["SECRET_KEY"]="4d8724c42e8a47b4be4edf6a1028b110"

@app.route("/")
def login_form():
    return render_template('login.html')

@app.route('/login_process', methods=['GET','POST'])
def logged():

  # Get the username and password from the form data
  username = request.form['username']
  password = request.form['password']

  # Call the login function and check if it returns true
  if login(username, password):
    # Redirect to the new page
    return redirect(url_for('newpage'))
  else:
    # Display an error message
    return redirect(url_for('login_form'))

@app.route('/logged')
def newpage():
  return render_template('logged.html')

app.run(debug=True)