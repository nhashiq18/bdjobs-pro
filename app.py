from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


books = []

age_ranges = ['0-10', '11-20', '21-30', '31-40', '41-50', '51+']
app.config['SECRET_KEY'] = '5445dfg65465f4654dfg54625fdg84'

@app.route('/')
def Home():
    return render_template('homepage.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form['book_name']
        publisher_name = request.form['publisher_name']
        age_range = request.form['age_range']
        num_pages = request.form['num_pages']
        date_of_publish = request.form['date_of_publish']
        
        # Append the book data to the list
        books.append({
            'book_name': book_name,
            'publisher_name': publisher_name,
            'age_range': age_range,
            'num_pages': num_pages,
            'date_of_publish': date_of_publish
        })
        flash(f'Item has been added!', 'success')
        return redirect(url_for('Home'))
    
    return render_template('add.html', books=books, age_ranges=age_ranges)

@app.route('/show')
def show():
    return render_template('show.html', books=books, age_ranges=age_ranges)

if __name__ == '__main__':
    app.run(debug=True)
