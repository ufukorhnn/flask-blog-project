from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Ufuk Orhan',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'March 1, 2022'
    },
    {
        'author': 'Fırat Orhan',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'March 2, 2022'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
