#author: Hafsah Mahmood
#class: CSE 30
#date: 12/08/23
class Vertex:
    #create a constructor for Vertex class
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
    #add another neighbor to the graph
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    #print out the vertex
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    #return which vertices are connected to which
    def getConnections(self):
        return self.connectedTo.keys()
    #return ID of the vertex
    def getId(self):
        return self.id
    #return the weight of the vertex
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    #create a constructor for class Graph
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    #add another vertex to the graph
    def addVertex(self,key):
        vertex = Vertex(key)
        self.vertList[key] = vertex
        self.numVertices += 1
    # return vertex if n is in the list
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    #check to see if a vertex is contained
    def __contains__(self,n):
        return n in self.vertList.values()
    # create an edge from f vertex to t vertex
    def addEdge(self,f,t,weight=0):
        fvertex = self.getVertex(f)
        tvertex = self.getVertex(t)
        fvertex.addNeighbor(tvertex)
    #return vertices of the graph
    def getVertices(self):
        return self.vertList.keys()
    #iterate through the graph
    def __iter__(self):
        return iter(self.vertList.values())
    #go to all nodes with the same distance first
    def breadth_first_search(self, s):
        visited = []
        queue   = []
        v = self.getVertex(s)
        visited.append(v.id)
        queue.append(v)

        while queue:
            s = queue.pop(0)
            for neighbour in s.getConnections():
                if neighbour.id not in visited:
                    visited.append(neighbour.id)
                    queue.append(neighbour)
        return visited
    #go to the furthest nodes, then come back and go to the next node
    def depth_first_search(self):
        return [f for f in self.getVertices()]
    #further DFS
    def DFS(self, vid, path):
        return self.depth_first_search()

#driver code
if __name__ == '__main__':
    #create a graph object g
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    #add edges onto graph
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)
    #prints verticies
    for v in g:
        print(v)
    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]
