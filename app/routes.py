from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
	user  = {'username' : 'senel'}
	posts = [
		{
			'author' : {'username' : 'John'},
			'body' : 'Beautiful day in Portland'
		},
		{
			'author' : {'username' : 'Susan'},
			'body'   : 'The avengers movie sucked'

		}
	]
	return render_template('index.html', title = 'home', posts = posts)

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	print(form)
	if form.validate_on_submit():
		print('validated loginform')
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('index'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	registForm = RegistrationForm()
	print(registForm)
	if registForm.validate_on_submit():
		user = User(username=registForm.username.data, email=registForm.email.data)
		user.set_password(registForm.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user')
		return redirect(url_for('index'))
	return render_template('register.html', title='Register', registForm=registForm)








