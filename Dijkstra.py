############################################
#     Dijkstra class (python 3)          #
############################################

from Graph import *
        
def shortestPath(Gr,root):
    Q = Gr.get_vertices() # Queue
    Gr.set_startNode(root) # start path

    while Q:
        Q.sort(key=lambda x : x.key)    # Sorts by key
        u = Q.pop(0)                    # Remove smallest key

        for v in list(u.adjacent.keys()):
            if v.key > u.key + u.adjacent[v] :
                v.key = u.key + u.adjacent[v]
                v.pi = u
    
def printPath(Gr, end):
    l = []
    current = Gr.G[end]
    while current != None :
        l.append(current.id)
        current = current.pi
    l.reverse()
    print (l)   

def reset(graph):
    for i in graph.get_vertices():
        i.key = infinity
        i.pi = None

'''
def main():
    g = Graph()  # Object Graph
    g.add_edge('A','B',10)
    g.add_edge('B','C',2)
    g.add_edge('D','C',1)
    g.add_edge('A','D',5)
    g.add_edge('D','B',3)
    
    shortestPath(g,'A')
    printPath(g,'C')
    printPath(g,'D')
    printPath(g,'B')
    reset(g)
    shortestPath(g, 'B')
    printPath(g,'C')
    printPath(g,'D')
    printPath(g,'A')

if __name__ == "__main__":

    main()
'''