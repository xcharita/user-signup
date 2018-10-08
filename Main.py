from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir))

app= Flask(__name__)
app.config['DEBUG'] = True
   

@app.route('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route('/signup', methods=['POST', 'GET'])
def Validate():
    username = request.form['username']
    password = request.form['password']
    ver_password = request.form['ver_password']
    email = request.form['email']
    template = jinja_env.get_template('index.html')
    user_error = ''
    pwd_error = ''
    email_error = ''
    check=3
 
    if ' ' in username:
        check -=1
        username=''
        user_error="No spaces are allowed in a username"
    
    if len(username) > 20:
        check -= 1
        username=''
        user_error="Username between 3 and 20 charachters please"
        
    if len(username) < 3:
        check -=1
        username=''
        user_error="Username between 3 and 20 charachters please"
    
    if len(username) == 0:
        check -= 2
        user_error="Enter a valid username between 3 and 20 charachters please"

    if len(password) == 0:
        check -=1
        pwd_error="You have no password!"
    
    if (password == ver_password) == False:
        check -= 2
        password= ''
        ver_password=''
        pwd_error="Password don't match"

    if len(email) >0 :
        if '@' in email:
            check += 1
            new_email= email.split('@')
            if len(new_email[0])<3:
                check -= 1
                email_error="Email is too short, use a min of 3 characters before @ please"
                email=''
            if len(new_email[0])>20:
                check -= 1
                email_error="Email is too long, use a max of 20 characters before @ please"
                email=''
            if len(new_email[1])<4:
                check -= 1
                email_error="Please enter a correct email" 
                email=''
        
        if Validate_email(email) == False: 
            check -= 1
            email_error="Please enter a correct email" 
            email=''

        if ' ' in email:
            check -= 1
            email_error="No spaces are allowed in an email"
            email=''
        
    else:
        check += 1
    
    if check > 3:
        template=jinja_env.get_template('welcome.html')
        return template.render(username=username)
    else:
        return template.render(username=username, user_error = user_error, password=password, pwd_error=pwd_error, ver_password=ver_password, 
        email=email, email_error=email_error)

def Validate_email(email):
    if ('.' in email):
        if ('@' in email):
            return True
    else:
        return False 


app.run()