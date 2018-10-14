
input = open("C-large.in", "r")
output = open("C-large.out", "w")


# # dijkstra implementation from https://gist.github.com/econchick/4666413
# class Graph:
#   def __init__(self):
#     self.nodes = set()
#     self.edges = defaultdict(list)
#     self.distances = {}
#
#   def add_node(self, value):
#     self.nodes.add(value)
#
#   def add_edge(self, from_node, to_node, distance):
#     self.edges[from_node].append(to_node)
#     self.edges[to_node].append(from_node)
#     self.distances[(from_node, to_node)] = distance
#
#
# def dijsktra(graph, initial):
#   visited = {initial: 0}
#   path = {}
#
#   nodes = set(graph.nodes)
#
#   while nodes:
#     min_node = None
#     for node in nodes:
#       if node in visited:
#         if min_node is None:
#           min_node = node
#         elif visited[node] < visited[min_node]:
#           min_node = node
#
#     if min_node is None:
#       break
#
#     nodes.remove(min_node)
#     current_weight = visited[min_node]
#
#     for edge in graph.edges[min_node]:
#       weight = current_weight + graph.distances[(min_node, edge)]
#       if edge not in visited or weight < visited[edge]:
#         visited[edge] = weight
#         path[edge] = min_node
#
#   return visited, path


# github.com/zaz/dijkstra
"""An efficient algorithm to find shortest paths between nodes in a graph."""
from collections import defaultdict

class Digraph(object):
    def __init__(self, nodes=[]):
        self.nodes = set()
        self.neighbours = defaultdict(set)
        self.dist = {}

    def addNode(self, *nodes):
        [self.nodes.add(n) for n in nodes]

    def addEdge(self, frm, to, d=1e309):
        self.addNode(frm, to)
        self.neighbours[frm].add(to)
        self.dist[ frm, to ] = d

    def dijkstra(self, start, maxD=1e309):
        """Returns a map of nodes to distance from start and a map of nodes to
        the neighbouring node that is closest to start."""
        # total distance from origin
        tdist = defaultdict(lambda: 1e309)
        tdist[start] = 0
        # neighbour that is nearest to the origin
        preceding_node = {}
        unvisited = self.nodes

        while unvisited:
            current = unvisited.intersection(tdist.keys())
            if not current: break
            min_node = min(current, key=tdist.get)
            unvisited.remove(min_node)

            for neighbour in self.neighbours[min_node]:
                d = tdist[min_node] + self.dist[min_node, neighbour]
                if tdist[neighbour] > d and maxD >= d:
                    tdist[neighbour] = d
                    preceding_node[neighbour] = min_node

        return tdist, preceding_node

    def min_path(self, start, end, maxD=1e309):
        """Returns the minimum distance and path from start to end."""
        tdist, preceding_node = self.dijkstra(start, maxD)
        dist = tdist[end]
        backpath = [end]
        try:
            while end != start:
                end = preceding_node[end]
                backpath.append(end)
            path = list(reversed(backpath))
        except KeyError:
            path = None

        return dist, path

    def dist_to(self, *args): return self.min_path(*args)[0]
    def path_to(self, *args): return self.min_path(*args)[1]


T = int(input.readline().strip())

for j in range(1, T+1):
    output.write("case #{}: ".format(j))
    line = input.readline().strip()
    N = int(line.split()[0])
    Q = int(line.split()[1])
    
    ponys = []
    for i in range(N):
    	line = input.readline().strip()
    	E = float(line.split()[0])
    	S = float(line.split()[1])	
    	ponys.append((E,S))

    edges = []
    for i in range(N):
    	line = input.readline().strip()
    	for j,d in enumerate(line.split()):
    		if int(d) != -1:
    			edges.append((i + 1, j + 1, float(d)))

    bla = []
    for r in range(Q):

        graph = Digraph()
        for k in range(N):
            graph.addNode((k + 1,))

        for i in range(N):
            graph1 = Digraph()
            for k in range(N):
                graph1.addNode((k+1,))

            for edge in edges:
                graph1.addEdge(edge[0], edge[1], edge[2])

            res, _ = graph1.dijkstra(i + 1)
            for j in res:
                if res[j] <= ponys[i][0] and res[j] != 0:
                    graph.addEdge(i + 1, j, res[j] / ponys[i][1])

        line = input.readline().strip()
        start = int(line.split()[0])
        end = int(line.split()[1])

        res, _ = graph.dijkstra(start)

        bla.append(res[end])

    output.write(" ".join([str(x) for x in bla]))
    output.write("\n")


input.close()
output.close()

