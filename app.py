from flask import Flask, render_template, request, redirect, url_for #Es para importar flask

app = Flask(__name__, template_folder='templates') #creamos una instancia de flask en una variable llamada app(se puede llamar como sea)

@app.route('/')#usamos un decorador(@) para crear una respuesta a la ruta / que es el index o página principal
def Hola(): #creamos la función que va a responder al llamado a  la ruta /
    return '<a href="/index">Página Principal</a>' #es lo que devuelve la función es este caso solo un texto (hola mundo)
@app.route('/plantilla')
def plantilla():
    data={
        'titulo':'Practica #2 con Bootstrap',
        'mensaje':'Bienvenido al sitio Web ',
        'nombre':'Dorian Fernando Galindo Salinas'
    } #Declaración de diccionario
    return render_template('layout.html',data=data) #render_template es para renderizar la plñantilla.

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')
@app.route('/personalData')
def personalData():
    return render_template('/personalData.html')

@app.route('/form', methods={"POST", "GET"})
def form():
    if request.method == 'POST':
        password = request.form["password"]
        email = request.form["correo"]
        name = request.form["name"]
        return redirect(url_for("data", password=password, email=email, name=name))
    else:
        return render_template('form.html')
    return render_template('/form.html')
@app.route('/<email>, <password>, <name>')
def data(password, email, name):
    data={
        'contraseña':password,
        'correo':email,
        'nombre':name
    }
    return render_template('/data.html', data=data)

app.run(debug=True) #es para correr la aplicación o sea nuestro sitio web en el servidor virtual

    
    
    #recuerda que para verlo solo debemos entrar a la dirección 127.0.0.1:5000 en cualquier navegador
    #es importante crear la carpeta templates porque ahi va flask a intentar buscar el archivo de la plantilla.