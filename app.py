from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    family_data = {
        'alex_name': 'Alex',
        'alex_age': 10,
        'alex_image': 'static/images/alex.jpg',
        'mom_name': 'Mom',
        'mom_age': 35,
        'mom_image': 'static/images/mom.jpg',
        'dad_name': 'Dad',
        'dad_age': 40,
        'dad_image': 'static/images/dad.jpg'
    }
    return render_template('index.html', **family_data)

if __name__ == '__main__':
    app.run(debug=True)
