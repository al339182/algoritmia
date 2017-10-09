
from algoritmia.datastructures.digraphs import UndirectedGraph
from labyrinthviewer import LabyrinthViewer

def load_labyrinth(fichero):
    filasFichero=[]
    fich=open(fichero)
    for line in fich:
        linea=line.split(",")
        filasFichero.append(linea)
    laberinto=[]
    i=0
    j=0
    for fila in filasFichero:
        for vertice in fila:
            if 'e' not in vertice:
                laberinto.append(((i,j),(i,j+1)))
            if 's' not in vertice:
                laberinto.append(((i,j),(i+1,j)))
            j+=1
        j=0
        i+=1
    devolver=UndirectedGraph(E= laberinto)
    return devolver

dev=load_labyrinth("laberinto-5x10.i")     
v=LabyrinthViewer(dev,canvas_width=900, canvas_height=600, margin=10)
v.run()
