from flask import Flask, render_template, request
from Vuelos_BFS import buscar_solucion_BFS

app = Flask(__name__)

# Grafo de conexiones
conexiones = {
    'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
    'Sonora': {'Zacatecas', 'Sinaloa'},
    'Guanajuato': {'Aguascalientes'},
    'Oaxaca': {'Queretaro'},
    'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
    'Celaya': {'Jiloyork', 'Sinaloa'},
    'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
    'Monterrey': {'Zacatecas', 'Sinaloa'},
    'Tamaulipas': {'Queretaro'},
    'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca', 'Monterrey'},
    'CDMX': set()
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        inicio = request.form["inicio"]
        destino = request.form["destino"]

        # Limpiar espacios
        inicio = inicio.strip()
        destino = destino.strip()

        # Validar ciudades
        if inicio not in conexiones or destino not in conexiones:
            resultado = "Ciudad no válida"
        else:
            nodo_solucion = buscar_solucion_BFS(conexiones, inicio, destino)

            if nodo_solucion is None:
                resultado = "No hay ruta disponible"
            else:
                camino = []
                nodo = nodo_solucion

                while nodo.get_padre() is not None:
                    camino.append(nodo.get_datos())
                    nodo = nodo.get_padre()

                camino.append(inicio)
                camino.reverse()

                resultado = camino

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run()