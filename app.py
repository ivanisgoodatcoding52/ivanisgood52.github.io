from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage with the form
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmPassword')
    month = request.form.get('month')
    day = request.form.get('day')
    year = request.form.get('year')
    gender = request.form.get('gender')

    # Basic validation
    if not username or len(username) < 3 or len(username) > 20:
        return "Error: Username must be between 3 and 20 characters."
    if not password or len(password) < 6 or password != confirm_password:
        return "Error: Passwords do not match or are too short."

    # Here you would normally store the information in a database
    # For now, we'll just log it to the console
    print(f"Username: {username}, Password: {password}, Birthday: {month} {day}, {year}, Gender: {gender}")
    
    # Redirect to a success page or show a success message
    return "Registration successful! Thank you for signing up."

if __name__ == '__main__':
    app.run(debug=True)
