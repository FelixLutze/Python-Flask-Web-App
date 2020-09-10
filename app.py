from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Felix L.',
        'title': 'Blog Post 1',
        'content': 'Example content.',
        'date': 'September 9, 2020'
    },
    {
        'author': 'Lutze F.',
        'title': 'Blog Post 2',
        'content': 'More example content.',
        'date': 'September 10, 2020'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, pageTitle="CustomHome")


@app.route('/about')
def about():
    return render_template('about.html', pageTitle="CostomAbout")


if __name__ == '__main__':
    app.run()
