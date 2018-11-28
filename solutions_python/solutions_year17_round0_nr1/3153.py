from pprint import pprint

class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        self.graph.setdefault(v, set())

    def add_edge(self, a, b):
        for start, end in ((a, b), (b, a)):
            edge = self.graph.setdefault(start, set())
            edge.add(end)

    def is_egde(self, a, b):
        if a not in self.graph:
            return False
        
        return b in self.graph[a]

    def __str__(self):
        return str(self.graph)


def convolute(row, flipper_size):
    def opp(x):
        return {'+': '-', '-': '+'}[x]

    for i in xrange(len(row) - flipper_size + 1):
        new_node = ''
        for j in xrange(len(row)):
            if j >= i and j < (i + flipper_size):
                new_node += opp(row[j])
            else:
                new_node += row[j]
        yield new_node


def bfs_paths(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for n in graph[vertex] - set(path):
            if n == goal:
                yield path + [n]
            elif n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


def solve(pancakes, flipper_size):
    if pancakes == '+' * len(pancakes):
        return 0

    g = Graph()
    
    to_add_fifo = [pancakes]
    while to_add_fifo:
        curr = to_add_fifo.pop(0)
        for v in convolute(curr, flipper_size):
            if not g.is_egde(curr, v):
                g.add_edge(curr, v)
                to_add_fifo.append(v)

    if '+' * len(pancakes) not in g.graph:
        return "IMPOSSIBLE"

    p = shortest_path(g.graph, 
                      pancakes,
                      '+' * len(pancakes))

    if p is None:
        return "IMPOSSIBLE"
    else:
        return len(p) - 1

def main():
    #print solve('-----', 5)
    #return
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        p, l = raw_input().split(" ")
        print "Case #{}: {} ".format(i, solve(p, int(l)))
        # check out .format's specification for more formatting options
    
    
if __name__ == '__main__':
    main()
