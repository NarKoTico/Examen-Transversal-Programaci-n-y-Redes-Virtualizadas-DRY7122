from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para registrar un nuevo usuario
@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    password = request.form['password'].encode('utf-8')
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    
    nuevo_usuario = Usuario(nombre=nombre, password_hash=password_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/validar', methods=['POST'])
def validar():
    nombre = request.form['nombre']
    password = request.form['password'].encode('utf-8')
    
    usuario = Usuario.query.filter_by(nombre=nombre).first()
    
    if usuario and bcrypt.checkpw(password, usuario.password_hash):
        return f'Bienvenido, {nombre}!'
    else:
        return 'Usuario o contraseña incorrectos.'

if __name__ == '__main__':
    app.run(port=5800)
