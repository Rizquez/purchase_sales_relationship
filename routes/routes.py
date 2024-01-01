from flask import Flask, render_template, redirect

# Iniciamos la app e indicamos la ubicacion para los ficheros HTML y CSS
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Manejador de errores mas comunes
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    return redirect('/error')



@app.route('/')
def home():
    return render_template('login.html')



@app.route('/error')
def error():
    return render_template("page_error.html")