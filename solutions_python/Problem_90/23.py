import fileinput
import psyco
psyco.full()

class priorityDictionary(dict):
    def __init__(self):
        '''Initialize priorityDictionary by creating binary heap
of pairs (value,key).  Note that changing or removing a dict entry will
not remove the old pair from the heap until it is found by smallest() or
until the heap is rebuilt.'''
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        '''Find smallest item after removing deleted items from heap.'''
        if len(self) == 0:
            raise IndexError, "smallest of empty priorityDictionary"
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
	
    def __iter__(self):
        '''Create destructive sorted iterator of priorityDictionary.'''
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
	
    def __setitem__(self,key,val):
        '''Change value stored in dictionary and add corresponding
pair to heap.  Rebuilds the heap if the number of deleted items grows
too large, to avoid memory leakage.'''
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  # builtin sort likely faster than O(n) heapify
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair
	
    def setdefault(self,key,val):
        '''Reimplement setdefault to call our customized __setitem__.'''
        if key not in self:
            self[key] = val
        return self[key]


class Node(object):
    def __init__(self, idx, maxDist):
        self.idx = idx
        self.neighbors = set()
        self.shortestParent = None
        self.distToTop = maxDist
    def __cmp__(self,other):
        return cmp(self.distToTop, other.distToTop)

class Graph(object):
    def __init__(self, numNodes):
        self.nodes = [Node(x,numNodes+1) for x in range(numNodes)]
        self.graphDict = {}
        for i in range(numNodes+1):
            self.graphDict[i] = {}
        self.seenPathes = {}

    def addNeighborPair(self,left,right):
        self.nodes[left].neighbors.add(right)
        self.nodes[right].neighbors.add(left)
        self.graphDict[left][right] = 1
        self.graphDict[right][left] = 1



    def Dijkstra(self,G,start,end=None):
        """
        Find shortest paths from the start vertex to all
        vertices nearer than or equal to the end.

	The input graph G is assumed to have the following
	representation: A vertex can be any object that can
	be used as an index into a dictionary.  G is a
	dictionary, indexed by vertices.  For any vertex v,
	G[v] is itself a dictionary, indexed by the neighbors
	of v.  For any edge v->w, G[v][w] is the length of
	the edge.  This is related to the representation in
	<http://www.python.org/doc/essays/graphs.html>
	where Guido van Rossum suggests representing graphs
	as dictionaries mapping vertices to lists of neighbors,
	however dictionaries of edges have many advantages
	over lists: they can store extra information (here,
	the lengths), they support fast existence tests,
	and they allow easy modification of the graph by edge
	insertion and removal.  Such modifications are not
	needed here but are important in other graph algorithms.
	Since dictionaries obey iterator protocol, a graph
	represented as described here could be handed without
	modification to an algorithm using Guido's representation.

	Of course, G and G[v] need not be Python dict objects;
	they can be any other object that obeys dict protocol,
	for instance a wrapper in which vertices are URLs
	and a call to G[v] loads the web page and finds its links.
	
	The output is a pair (D,P) where D[v] is the distance
	from start to v and P[v] is the predecessor of v along
	the shortest path from s to v.
	
	Dijkstra's algorithm is only guaranteed to work correctly
	when all edge lengths are positive. This code does not
	verify this property for all edges (only the edges seen
 	before the end vertex is reached), but will correctly
	compute shortest paths even for some graphs with negative
	edges, and will raise an exception if it discovers that
	a negative edge has caused it to make a mistake.
	"""

	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
        #print start
	Q[start] = 0
	
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = set([v])
                        elif vwLength == Q[w]:
                            P[w].add(v)
	
	return (D,P)

    def calcValueOfPath(self, D, P, curPoint):
        #print "Handling point",curPoint
        if curPoint in self.seenPathes:
            return self.seenPathes[curPoint]
        threatSets = set()
        ourSet = set([x for x in self.nodes[curPoint].neighbors if x != 0])
        if curPoint == 1:
            ourSet = set()
        if curPoint == 0:
            threatSets.add(frozenset(ourSet))
        else:
            for prev in P[curPoint]:
                for ps in self.calcValueOfPath(D,P,prev):
                    threatSets.add(frozenset(ps.union(ourSet)))
        self.seenPathes[curPoint] = threatSets
        #print "Returning threat set:",threatSets, "for point",curPoint
        return threatSets

    def runDijkstra(self):
        D, P = self.Dijkstra(self.graphDict,0)
        t = self.calcValueOfPath(D,P,1)
        return D[1],max(len(x) for x in t)

def handleCase(it, idx):
    numNodes, numWormHoles = [int(x) for x in it.next().split()]
    g = Graph(numNodes)
    whRaw = [x for x in it.next().split()]
    for w in whRaw:
        begin,end = [int(x) for x in w.split(",")]
        g.addNeighborPair(begin,end)
    c,t = g.runDijkstra()
    print "Case #%d: %d %d" % (idx,c-1,t-c+1)

def main():
    it = fileinput.input()
    nc = int(it.next())
    for i in range(nc):
        handleCase(it,i+1)

main()
