# puzzle lineal con busqueda en amplitud
# 
from arbol import Nodo 

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frotera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frotera.append(nodo_inicial)
    while (not solucionado) and len (nodos_frotera) != 0:
        nodo = nodos_frotera.pop(0)
        # Extraer el nodo y añadirlo a visitados 
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucion = True
            return nodo
        else: 
            # Expandir nodos hijo
            dato_noto = nodo.get_datos()

            #Operador Izquierdo 
            hijo = [dato_noto[1], dato_noto[0], dato_noto[2],dato_noto[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados)and not hijo_izquierdo.en_lista(nodos_frotera):
                nodos_frotera.append(hijo_izquierdo)
            
            # Operador central
            hijo = [dato_noto[0], dato_noto[2], dato_noto[1],dato_noto[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados)and not hijo_central.en_lista(nodos_frotera):
                nodos_frotera.append(hijo_central)

            #Operador Derecho
            hijo = [dato_noto[0], dato_noto[1], dato_noto[3],dato_noto[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados)and not hijo_derecho.en_lista(nodos_frotera):
                nodos_frotera.append(hijo_derecho)

            nodo.set_hijos ([hijo_izquierdo, hijo_central, hijo_derecho])
if __name__ == "__main__":
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial,solucion)

    # Mostrar el resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
            
            