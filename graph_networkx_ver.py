'''
Program implementing an unidirected graph with weighted edges
using adjacency matrix method and visualize such graph.

Author: Roid
'''
import networkx as nx
import matplotlib.pyplot as plt


#   Takes input from the file and creates a weighted undirected graph
def newGraph():
        G = nx.Graph()
        f = open('graph_input.txt')
        n = int(f.readline())
        weightedMatrix = []
        for i in range(n):
            #   Read from each i until n, split between spaces and func is int
            #   creates a direct conversion to int same as line 9
            #   map func will return a list, can be appended into weightedMatrix
            listing = map(int, (f.readline()).split())
            #print(listing)
            weightedMatrix.append(listing)

        #   Adds egdes along with their weights to the graph 
        for i in range(n) :
            for j in range(n):
                if weightedMatrix[i][j] > 0 :
                        #   Edges - (node1,node2,weightVal)
                        G.add_edge(i, j, length = weightedMatrix[i][j])
        return G #  Returns object graph

def displayGraph(G,color):
        #   pos returns a dictionary type of nodes as keys, positions as val.
        #   *optional* as it depends on layout of graph required.
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels = True, edge_color = 'black',node_color = color,font_weight = 'bold')
        #nx.draw(G,pos = None,with_labels = True, edge_color = color)
        #   Find the 'length' passing var in G 
        edge_label = nx.get_edge_attributes(G,'length')

        #   Prints weight on all the edges
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_label,font_size = 12,font_weight = 'bold')
        return pos

G = newGraph()
#print(type(G))
plt.figure(1)
D = displayGraph(G,'purple')
#print(type(D))
#print(nx.has_path(G,3,6))
print("SHORTEST ROUTE:",nx.shortest_path(G,3,6))
for e in nx.all_shortest_paths(G,source = 3, target = 6):
    print(e)
print
print(nx.dijkstra_path(G,source = 3, target = 6))
plt.show()
