from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you would typically collect the form data
        # and send an email or store it in a database
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Add logic to handle the data, such as sending an email
        # For now, let's just print it to the console
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Redirect to a new URL or display a success message
        return redirect(url_for('thank_you'))

    # If method is GET or form wasn't submitted, just render the contact page
    return render_template('contact.html')

