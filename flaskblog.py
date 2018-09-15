from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#prevent modify cookie
app.config['SECRET_KEY'] = 'eaf2b29a66444de11bb49ebad5dd14e2'

posts = [
    {
        'author': 'tawan',
        'title': 'heyyy this is title',
        'content': 'my first dummy',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'natachit',
        'title': 'this is also title',
        'content': 'my second dummy',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)


