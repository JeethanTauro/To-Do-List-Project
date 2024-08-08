from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime  import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'
db = SQLAlchemy(app)

class Todo(db.Model):
    no = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200) , nullable = False)
    desc = db.Column(db.String(500) , nullable = True)
    date_created = db.Column(db.DateTime,  default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.no} - {self.title}"




@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
       title =  request.form['title']
       desc =  request.form['desc']
       if not title or not desc:
            flash('Title and Description cannot be empty!', 'warning')
            return redirect(url_for('home'))
       else:
            todo = Todo(title = title , desc = desc)
            db.session.add(todo)
            db.session.commit()
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo = alltodo)

@app.route('/update/<int:no>', methods = ['POST', 'GET'])
def update(no):
    todo = Todo.query.filter_by(no=no).first()
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if not title or not desc:
            flash('Title and Description cannot be empty!', 'warning')
            return redirect(url_for('update', no=no))
        else:
            todo.title = title
            todo.desc = desc
            db.session.commit()
            flash('Todo updated successfully!', 'success')
            return redirect(url_for("home"))
    return render_template('update.html',todo=todo)

@app.route('/delete/<int:no>')
def delete(no):
    todo = Todo.query.filter_by(no=no).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)