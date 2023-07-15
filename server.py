from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')  # decorator
def my_home():
    return render_template('index.html')


@app.route('/about.html')  # decorator
def about():
    return render_template('about.html')


@app.route('/works.html')  # decorator
def work():
    return render_template('works.html')


@app.route('/contact.html')  # decorator
def contact():
    return render_template('contact.html')


@app.route('/home')  # decorator
def home():
    return render_template('index.html')


@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        fieldnames = ['email', 'subject', 'message']

        csv_writer = csv.DictWriter(database2, fieldnames=fieldnames)

        # Check if the file is empty and write the header if necessary
        if database2.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerow(
            {'email': email, 'subject': subject, 'message': message})


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again'


if __name__ == '__main__':
    app.run(debug=True)
