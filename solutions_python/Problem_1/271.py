#!/usr/bin/python2.5
# Solution to Google Code Jam 08 Problem A
# Matt Giuca

# Usage: ./probA.py < inputfile > outputfile

# Dijkstra's algorithm based on pseudo-code from:
# http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# Retrieved on 17/7/2008

import sys

DEBUG = False

def parse(file=sys.stdin):
    """
    (Generator) Read input file from filename or file or stdin,
    return a structure.
    Yields (list of str, list of str) pairs.
    (First is set of search engine names, second is list of queries).
    """
    if isinstance(file, basestring):
        file = open(file)
        toclose = True
    else:
        toclose = False
    n = int(file.readline().strip())
    for i in range(n):
        engines = []
        queries = []
        s = int(file.readline().strip())
        for j in range(s):
            engines.append(file.readline().strip())
        q = int(file.readline().strip())
        for j in range(q):
            queries.append(file.readline().strip())
        yield engines, queries
    if toclose:
        file.close()

class Node(object):
    """
    Graph node.
    """
    def __init__(self, name=None):
        self.name = name
        self.edges = []
    def __repr__(self):
        return "Node(%r)" % self.name
    def add_edge(self, node):
        self.edges.append(node)

def make_sample_graph():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    a.add_edge(b)
    a.add_edge(c)
    b.add_edge(d)
    c.add_edge(e)
    d.add_edge(e)
    return [a, b, c, d, e], a, e
sample_graph, sample_graph_start, sample_graph_end = make_sample_graph()

class DijkstraError(Exception):
    pass

def dijkstra(graph, startnode, endnode):
    """
    Dijkstra's algorithm.
    graph: List of Nodes.
    startnode, endnode: Node
    Returns a list of nodes from startnode to endnode containing the shortest
    path.
    Raises a DijkstraError if there are no paths to the end.
    """
    for v in graph:
        v.dist = len(graph)     # Infinity
        v.previous = None
    startnode.dist = 0
    q = set(graph)              # All unoptimised nodes in graph
    while len(q) > 0:
        u = min(q, key=lambda n: n.dist)    # Node with smallest dist
        q.remove(u)
        for v in u.edges:
            if v in q:
                alt = u.dist + 1            # 1 is dist between u and v
                if alt < v.dist:
                    v.dist = alt
                    v.previous = u

    curnode = endnode
    pathlist = [curnode]
    while curnode is not startnode:
        if curnode.previous is None:
            raise DijkstraError("No path found from start to end")
        curnode = curnode.previous
        pathlist.append(curnode)
    return pathlist[::-1]

def solve_case(engines, queries):
    """
    Given a list of engines and a list of queries, returns an int, the number
    of switches required.
    """
    graph = []      # List of all nodes
    startnode = Node("Start")
    endnode = Node("End")
    graph.append(startnode)
    graph.append(endnode)
    # Make an initial node for each engine (no query yet)
    curnodes = [Node(e) for e in engines]
    # Make a dict mapping engine names to indices in the curnodes array
    i = 0
    engine_indices = {}
    for engine in engines:
        engine_indices[engine] = i
        i += 1

    for node in curnodes:
        startnode.add_edge(node)
        graph.append(node)

    # Add a new node for each query matching an engine
    for query in queries:
        try:
            index = engine_indices[query]
        except KeyError:
            # Query doesn't match an engine name; not important
            continue
        # curnodes[index] is going to end, and link to all other curnodeses
        for i in xrange(len(curnodes)):
            if i != index:
                curnodes[index].add_edge(curnodes[i])
        # replace curnodes[index] with a new node
        curnodes[index] = Node(curnodes[index].name)
        graph.append(curnodes[index])

    # All current nodes point to the end node
    for i in xrange(len(curnodes)):
        curnodes[i].add_edge(endnode)

    # Apply Dijkstra's algorithm (gets a list of nodes, the optimal path)
    path = dijkstra(graph, startnode, endnode)

    if DEBUG:
        print path

    # The path now contains start -> first -> others ... -> end
    # We only want to count others (start and end are dummy nodes, and first
    # doesn't count as a switch).
    return len(path)-3

def do_all(file=sys.stdin):
    """
    Processes input, prints output to stdout.
    """
    i = 0
    for engines, queries in parse(file):
        i += 1
        answer = solve_case(engines, queries)
        print("Case #%d: %d" % (i, answer))

if __name__ == "__main__":
    do_all()
