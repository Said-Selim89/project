from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models.info import Info
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
db.init_app(app)

@app.route('/')
def home():
    tip = Info.query.all()
    return render_template('index.html', infos=tip)


@app.route('/create_base', methods=['POST'])
def base():
    title = request.form.get('title')
    text = request.form.get('text')
    info = Info(title=title, text=text)
    db.session.add(info)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    info = db.session.get(Info, id)
    db.session.delete(info)
    db.session.commit()
    return redirect('/')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)