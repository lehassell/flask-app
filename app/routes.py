from io import BytesIO
from flask import render_template, Flask, make_response, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from app import app
import matplotlib.pyplot as plt

@app.route('/')
@app.route('/index')

def index():
    user = {'username' : 'Ed'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title = "home", user = user, posts = posts)

@app.route("/fig/")
def fig():
    # Generate image
    fig, ax = plt.subplots(1)
    plt.plot(range(10))
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/image/')
def images():
    return render_template("image.html")


@app.route("/contact")
def contact():

