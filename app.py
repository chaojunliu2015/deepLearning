from flask import Flask, render_template
#import Requests


app = Flask(__name__)

@app.route('/')
def myHomePage():
    return render_template('home.html')

if __name__ == '__main()__':

    app.run(debug=True)
    #

