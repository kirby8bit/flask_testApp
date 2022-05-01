
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    tasks = ['sign in','sign up','about']
    return render_template('index.html',tasks=tasks)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/auth",methods=['POST','GET'])
def auth():
    return render_template('auth.html')

@app.route("/profile/<username>")
def profile(username):
    return render_template('user.html',username=username)



@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')



if __name__ == '__main__':
    app.run(debug=True)