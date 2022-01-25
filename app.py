import enum
import tkinter
from crypt import methods
from turtle import title
from flask import Flask, jsonify, request
app =Flask(__name__)
books_list = [
    {  
        "id": 1,
        "author": "Samuel Becket",
        "language": "English",
        "title": "Molloy the fairy tale",
    },
    {
         "id": 2,
         "author": "Apiko man",
         "language": "swahili",
         "title": "the bodaboda rider",
    },
    {
         "id": 3,
         "author": "Steve Bonnucci",
         "language": "Italian",
        "title": "Pasta",
         },
    {
         "id": 4,
         "author": "Toto vifalmwe",
         "language": "buganda",
         "title": "viva la viva",
    },
    {
         "id": 5,
         "author": "Chozi la Heri",
         "language": "Swahili",
         "title": "Mlima wa Mambondeni",
    },
    {   
         "id": 6,
         "author": "Romanus Bett",
         "language": "English",
         "title": "The BazookaMan",
    },
  ]

@app.route("/")
def home():
    return "Hello world"
@app.route("/books", methods=['GET', 'POST'])
def books():
      if request.method == 'GET':
          if len(books_list)>0:
              return jsonify(books_list)
          else:
              "Nothing found",404

      if request.method == 'POST':
          new_author = request.form['author']
          new_lang = request.form['language']
          new_title = request.form['title']
          iD = books_list[-1]['id']+1

          new_Obj = {
              "id": iD,
              "title": new_title,
              "language": new_lang,
              "author": new_author,
          }
          books_list.append(new_Obj)
          return jsonify(books_list), 201


@app.route("/book/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book["id"] == id:
                return jsonify(book) 
            pass
    if request.method =='PUT':
        for book in books_list:
            if book["id"] == id:
                book["author"] = request.form["author"]
                book["title"] = request.form["title"]
                book["language"] = request.form["language"]
                updated_book = {
                    "id": id,
                    "language":book["author"],
                    "title": book["title"],
                    "author":book["author"]
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book["id"] == id:
                books_list.pop(index)
                return jsonify(books_list)
if __name__=="__main__":
    app.run(debug=True)