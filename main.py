# import sqlite3
#
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books ("
# #                "id INTEGER PRIMARY KEY,"
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250)NOT NULL "
# #                "NULL, rating FLOAT NOT NULL)")
#
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(16), unique=True, nullable=False)
    author = db.Column(db.String(16), nullable=False)
    rating = db.Column(db.Float)


with app.app_context():
    db.create_all()

    # book = Books(
    #     title="Harry Pos",
    #     author="J. K.Rosasdsaswlfing",
    #     rating=9.3
    # )
    # db.session.add(book)
    # db.session.commit()

    data = db.session.execute(db.select(Books).order_by(Books.author)).scalars()
    for n in data:
        print(f"{n.author}, - {n.title} -  {n.rating}")
if __name__ == '__main__':
    app.run(debug=True)
