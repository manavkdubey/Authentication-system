from flask import Flask, flash, redirect, render_template, request, url_for

import json

def login_username(username):
    # Load the user cred from the JSON file
    with open('static\cred.json', 'r') as f:
        cred = json.load(f)

    # Check if the username match
    for user in cred['users']:
        if user['username'] == username:
            # Login successful
            return True
    
    # Login failed
    return False

def login_password(password):
    # Load the user cred from the JSON file
    with open('static\cred.json', 'r') as f:
        cred = json.load(f)

    # Check if the password match
    for user in cred['users']:
        if user['password'] == password:
            # Login successful
            return True
    
    # Login failed
    return False


app = Flask(__name__)
app.config["SECRET_KEY"]="4d8724c42e8a47b4be4edf6a1028b110"

@app.route("/")
def main_form():
    return render_template('main.html')

@app.route("/register")
def register_form():
    return render_template('register.html')


@app.route("/login-username")
def login_form_username():
    return render_template('login-username.html')

@app.route("/login-password")
def login_form_password():
    return render_template('login-password.html')

@app.route('/login_process_username', methods=['GET','POST'])
def logged_username():

  # Get the username and password from the form cred
  username = request.form['username']

  # Call the login function and check if it returns true
  if login_username(username):
    # Redirect to the new page
    return redirect(url_for('login_form_password'))
  else:
    # Display an error message
    flash("Invalid username or password","error")

    
    return redirect(url_for('login_form_username'))

@app.route('/login_process_password', methods=['GET','POST'])
def logged_password():

  # Get the username and password from the form cred
  
  password = request.form['password']

  # Call the login function and check if it returns true
  if login_password(password):
    # Redirect to the new page
    return redirect(url_for('newpage'))
  else:
    # Display an error message
    flash("Invalid username or password","error")

    
    return redirect(url_for('login_form_password'))

@app.route('/logged')
def newpage():
  return render_template('logged.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    username = request.form['username']
    password = request.form['password']

    with open('static\cred.json', 'r') as f:
        cred = json.load(f)

    cred_list = cred.get('users', [])  # get the list of users or create a new one if it doesn't exist

    cred_list.append({
        'username': username,
        'password': password
    })

    cred['users'] = cred_list  # update the 'users' key with the updated list of users

    with open('static\cred.json', 'w') as f:
        json.dump(cred, f)

    return redirect('/logged')

app.run(debug=True)