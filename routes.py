from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from forms import UsersForm, DeleteUserForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = UsersForm()
    if request.method == 'GET':
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            age = request.form['age']
            email = request.form['email']
            new_user = User(first_name=first_name, last_name=last_name, age=age, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

@app.route('/view-users')
def view_users():
        userslist = User.query.all()    
        return render_template('view_users.html', users=userslist)

@app.route('/delete-user')
def delete_users():
    
        User.query.filter(User.user_id == request.args.get('userId')).delete()
        db.session.commit()
        userslist = User.query.all()    
        return render_template('view_users.html', users=userslist)

@app.route('/edit-user', methods=['GET', 'POST'])
def edit_user():
    form = UsersForm()
    if request.method == 'GET':
        my_user = User.query.filter(User.user_id == request.args.get('userId')).first()
        form.first_name.data = my_user.first_name
        form.last_name.data = my_user.last_name
        form.email.data = my_user.email
        form.age.data = my_user.age
        return render_template('edit_user.html', form=form, user=my_user)
    else:
        if form.validate_on_submit():
            updated_user = User.query.filter(User.user_id == request.args.get('userId')).first()
            updated_user.first_name = request.form['first_name']
            updated_user.last_name = request.form['last_name']
            updated_user.age = request.form['age']
            updated_user.email = request.form['email']
            db.session.commit()
            
            userslist = User.query.all()    
            return render_template('view_users.html', users=userslist)

if __name__ == "__main__":
  app.run()

  #    db.session.query(Users).all();
