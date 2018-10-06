from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        template_dir))

app= Flask(__name__)
app.config['DEBUG'] = True
   

@app.route('/', methods=['GET'])
def index():
    template = jinja_env.get_template('index.html')
    return template.render()


@app.route('/welcome', methods=['POST','GET'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render('welcome.html', name=username)

'''
@app.route("/signup", methods=['POST'])
def Validate():
    usr_val= request.form['username']
#   pwd_val = request.form['password']
#    pwd_val_ver = request.form['password_ver']
#    email_val = request.form['email']
    user_error = ''

    len_usr_val = len(usr_val)


    if (len_usr_val <= 3) or (len_usr_val > 20):
        user_error = "Please enter a valid username (between 3 and 20 characters)"
        username=''
    if ' ' in usr_val:
        user_error = "Please enter a valid username (between 3 and 20 characters)"
        username=''
#    if (pwd_val == pwd_val_ver):
#        password_error = "The passwords don't match, please try again"
    
    if (user_error == ''):
        return "Thank you for submitting"
    else:
        return form.format()
    

'''


app.run()