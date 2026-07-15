from flask import Flask, render_template, redirect, request
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from database import db
from models.info import Info
from models.user import User

app = Flask(__name__)

# Настройки
app.config["SECRET_KEY"] = "..."
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///info.db"

db.init_app(app)

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ===== Главная =====   

@app.route("/")
def home():
    return render_template('index.html')


# ===== Регистрация =====
@app.route("/register")
def register():
    return render_template('registr.html')


@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user:
        return'ползователь существует'
    hached_password = generate_password_hash(password)
    new_user = User(username=username,
                    password=hached_password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')


# ===== Вход =====

@app.route("/login", methods=["GET", "POST"])
def login():
    ...


# ===== Выход =====

@app.route("/logout")
def logout():
    ... 


# ===== CRUD =====

@app.route("/create", methods=["POST"])
def create():
    ...


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    ...


@app.route("/delete/<int:id>")
def delete(id):
    ...


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)