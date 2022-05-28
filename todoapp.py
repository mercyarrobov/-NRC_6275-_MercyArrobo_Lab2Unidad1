
#Importar Flask
from flask import Flask, render_template
#Instanciar a la aplicación
app = Flask(__name__)
#Lista dónde se almacenará las tareas pendientes
lista = []

#Define la ruta principal
@app.route('/')

#Función para llamar a la página index.html
def index():
    return render_template()

#Define la ruta enviar
@app.route('/enviar')

#Función para enviar la lista
def enviar():
    return

#Define la ruta borrar
@app.route('/borrar')

#Función para borrar la lista
def borrar():
    return

#main del programa 
if __name__ == "__main__":
	app.run(debug=True)
