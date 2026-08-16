from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Variables simuladas desde el backend
    usuario = "Francisco Cáceres"
    materia = "Prácticas Profesionalizantes III"
    
    # Lista de objetos para iterar dinámicamente en la plantilla
    modulos = [
        {"nombre": "Computación en la Nube", "estado": "Completado"},
        {"nombre": "Control de Versiones (Git)", "estado": "Completado"},
        {"nombre": "Plantillas Dinámicas (Flask)", "estado": "En Proceso"}
    ]
    
    # Pasaje de datos a la plantilla HTML
    return render_template('index.html', usuario=usuario, materia=materia, modulos=modulos)

if __name__ == '__main__':
    app.run(debug=True)