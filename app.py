from flask import Flask, render_template

app = Flask(__name__)

titles = [
    {
        'name': 'First title'
    },
    {
        'name': 'Second title'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', titles=titles)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
