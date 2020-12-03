# from flask import Flask

from flask import Flask, render_template
from flask import Flask, render_template, json, request
from flask import abort, redirect, url_for
import pandas as pd
from sklearn import linear_model

application = Flask(__name__)
app = Flask(__name__)


def predict(abc):
    df_house = pd.read_csv('house-price.csv', sep =";")
    X = df_house[['square_feet']]
    Y = df_house['house_price']
    # with sklearn
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    new_square_feet = abc
    pred = str(regr.predict([[new_square_feet]]))
    pred = pred.replace('[','').replace(']','')
    return pred

def predict_diabetes(preg,glu,blp,skn,ins,bni,dbf,age):
    df = pd.read_csv('diabetes.csv')
    x = df.drop('Outcome', axis=1)
    y = df['Outcome']
    from sklearn.model_selection import train_test_split, cross_val_score
    x_train, x_test, y_train, y_test  = train_test_split(x , y, shuffle = True, test_size=0.3, random_state=1)
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=7)
    model.fit(x,y)
    x_pred = [preg,glu,blp,skn,ins,bni,dbf,age]
    return model.predict([x_pred,x_pred])[0]

# def index():
#     return f"""<h1> {pred} </h1>"""
@application.route('/')
def index():
        return render_template('index.html')

@application.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST":
       # first_name = int(request.form.get("fname"))
        a = int(request.form.get("pregnancies"))
        b = int(request.form.get("glucose"))
        c = int(request.form.get("bloodpressure"))
        d = int(request.form.get("skinthickness"))
        e = int(request.form.get("insulin"))
        f = int(request.form.get("bmi"))
        g = int(request.form.get("dbf"))
        h = int(request.form.get("age"))
        pre = predict_diabetes(a,b,c,d,e,f,g,h)
        return render_template("login.html", name=pre)
    return render_template("login.html")


if __name__ == '__main__':
    application.run(debug=True)


# with application.test_request_context():
#     print(url_for('index'))
#     print(url_for('hello'))
#     # print(url_for('login', next='/'))
#     # print(url_for('profile', username='John Doe'))
# from markupsafe import escape
#
# @application.route('/abc/<username>')
# def abc(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)
# @application.route('/showSignUp')
# def showSignUp():
#     return render_template('signup.html')
#
# from markupsafe import escape
#
# @application.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)
#
# @application.route('/signUp',methods=['POST'])
# def signUp():
#     # read the posted values from the UI
#     _name = request.form['inputName']
#     _email = request.form['inputEmail']
#     _password = request.form['inputPassword']
#
#     if _name and _email and _password:
#         return json.dumps({'html':'<span>All fields good !!</span>'})
#     else:
#         return json.dumps({'html':'<span>Enter the required fields</span>'})
#
# @application.route('/hello')
# @application.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
