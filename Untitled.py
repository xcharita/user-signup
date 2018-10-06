from flask import Flask, request, redirect
#from validate_email import validate_email

app= Flask(__name__)
app.config['DEBUG'] = True
   
form = """
<!doctype html>
<html>
<head><font size="+2"><b>Sign-up</b></font></head><br><br>
    <style type="text/css">
        .error{{color:red;}}
    </style>
    <body>

        <form action = "/signup" method='POST'>
            <label for="username" >Username &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                <input id="username" type="text" name="username"  value='{username}' /><br>
            </label>
           
            <label for="password">Password &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                <input id="password" type="password" name="password" value='{password}' /><br>
            </label>
            
            <label for="ver_password">Verify Password
                <input id="ver_password" type="password" name="ver_password" value='{password_ver}'/><br>
            </label>
            
            <label for="email">Email (optional) 
                <input id="email" type="text" name="email" value='{email}' /><br>
            </label>

            <input type="submit" value="Sign me up!"/>
            <p class="error">{user_error}</p>
            <p class="error">{password_error}</p>
            <p class="error">{password_ver_error}</p>
            <p class="error">{email_error}</p>
        </form>

    </body>
</head>
</html>

"""


@app.route("/signup")
def Signup():
    return form.format(username='', password='', user_error='', password_error='', 
            password_ver='', password_ver_error='', email='', email_error='')


@app.route("/signup", methods=['POST'])
def Validate():
    usr_val= request.form['username']
#   pwd_val = request.form['password']
#    pwd_val_ver = request.form['password_ver']
#    email_val = request.form['email']
    user_error = ''
    password_error = ''
    email_error = ''
    len_usr_val = len(usr_val)


    if (len_usr_val <= 3) or (len_usr_val > 20):
        user_error = "Please enter a valid username (between 3 and 20 characters)"
        username=''
    if ' ' in usr_val:
        user_error = "Please enter a valid username (between 3 and 20 characters)"
        username=''
#    if (pwd_val == pwd_val_ver):
#        password_error = "The passwords don't match, please try again"
    
    if (user_error == '' and password_error == ''):
        return "Thank you for submitting"
    else:
        return form.format(user_error=user_error,
            password_error=password_error, username=username)
    

'''


app.run()