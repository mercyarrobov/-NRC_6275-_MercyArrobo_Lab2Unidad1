
#Importar Flask
from flask import Flask, render_template, request, redirect
# Instancia de Flask. Aplicación
app = Flask(__name__, template_folder='template')

#Lista dónde se almacenará las tareas pendientes
lista= []

#Define la ruta principal
@app.route('/')

#Función para llamar a la página index.html
def index():
	return render_template("index.html", lista=lista)

#Define la ruta enviar y para que acepte las peticiones POST.
@app.route('/enviar', methods=[ 'POST'])

#Función para enviar la lista
def enviar():
	if request.method == 'POST':
		#Obtenemos el valor de los campos tarea
		# Esto lo hacemos con el diccionario "form"
		tarea = request.form.get('tareaI')
		lista.append(tarea)
		# Retornamos la respuesta a la página index
		return redirect('/')

#Define la ruta borrar, y para que acepte las peticiones POST.
@app.route("/borrar", methods=['POST'])

#Función para borrar la lista
def borrar():
    if request.method == 'POST':
		#Obtenemos el valor de los campos tarea
		# Esto lo hacemos con el diccionario "form"
        tarea = request.form.get('tareaB')
        lista.remove(tarea) 
		# Retornamos la respuesta a la página index
        return redirect('/')

#main del programa 
if __name__ == "__main__":
	# Iniciamos la apicación en modo debug
	app.run(debug=True)