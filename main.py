from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

# -----------MODELOS-------------

from models.modelsUser import ModelUser

#_---------ENTITIES---------------

from models.entities.User import User

#------------APP Flask-------------------------------------------------------------

app=Flask(__name__)
db=MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
	return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method=='POST':

		user = User(0, request.form['username'], request.form['password'])
		logged_user=ModelUser.login(db, user)

		if logged_user != None:
			if logged_user.password:
				login_user(logged_user)
				return redirect(url_for('inicio'))
			else:
				flash("Contraseña no valida")
				return render_template('auth/login.html')
		else:
			flash("Usuario no encontrado...")
			return render_template('auth/login.html')
	else:
		return render_template('auth/login.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/inicio')
def inicio():
	return(render_template('layout.html'))

if __name__=='__main__':
	app.config.from_object(config['development'])
	app.run(port=8000)