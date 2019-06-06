# -*- coding: utf8 -*-
# Python 3.7
# @author 3ngineer2k8

import networkx as nx # librería para usar grafos
import matplotlib.pyplot as plt # librería para dibujar

G = nx.Graph() # se crea un grafo vacío sin nodos y aristas
H = nx.path_graph(4) # 4 nodos
G.add_nodes_from(H) # lista de nodos (A,B,C,D) donde A=0 B=1 C=2 D=3
G.add_edges_from([(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)]) # lista de aristas
#               ([(A,B),(B,C),(C,D),(D,A),(A,C),(B,D)]) 
#               ([(e1 ),(e2 ),(e3 ),(e4 ),(e5 ),(e6 )])
# ver cantidad de nodos y aristas
print('Cantidad de nodos:',G.number_of_nodes())
print('Cantidad de aristas:',G.number_of_edges())
# Ver nodos y aristas del grafo
print('Nodos: \n',list(G.nodes))   # ver nodos
print('Aristas: \n',list(G.edges)) # ver aristas
# ver adyacencias de los nodos
print('Adyacencias de A: \n',list(G.adj[0])) # ver adyacencias para el nodo A o 0
print('Adyacencias de B: \n',list(G.adj[1])) # ver adyacencias para el nodo B o 1
print('Adyacencias de C: \n',list(G.adj[2])) # ver adyacencias para el nodo C o 2
print('Adyacencias de D: \n',list(G.adj[3])) # ver adyacencias para el nodo D o 3
# Visualizar el grafo
nx.draw(G)  # dibujar grafo
plt.title('Grafo del mapa con 4 distritos',fontsize=16) # titulo 
plt.axis('off')  # ocultar ejes
plt.show()  # mostrar dibujo









