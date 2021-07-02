
from flask import Flask,render_template,url_for,redirect,request
import model

app = Flask(__name__)


book_title_list=model.book_title_list

@app.route('/',methods = ['POST','GET'])
@app.route('/home',methods = ['POST','GET'])
def home():
    return render_template("home.html")


@app.route('/knn1',methods = ['POST','GET'])
def knn1():
    if request.method == 'POST':
        selected_book = request.form['book-name-knn']
        return redirect(url_for('knn',knn= selected_book ))

    else:
        return render_template("knn1.html",book_list =book_title_list)

@app.route('/svd',methods = ['POST','GET'])
def svd():
    if request.method == 'POST':
        selected_book = request.form['book-name']
        return redirect(url_for('book',book= selected_book ))

    else:
        return render_template("svd.html",book_list =book_title_list)


@app.route('/<book>')
def book(book):
    final_list=model.bookRecommendation(book)
    url_list=model.imgUrlList(final_list)
    return render_template('book.html',final_list=final_list,book_selected=book,url_list=url_list)

@app.route('/<knn>_test')
def knn(knn):
    final_book_list=model.methodTwo(knn)
    url_list=model.imgUrlList(final_book_list)
    return render_template('knn.html',final_book_list=final_book_list,book_selected=knn,url_list=url_list)






@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)