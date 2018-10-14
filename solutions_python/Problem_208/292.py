from codejam import CodeJam

from bisect import insort

class graph(object):
    def __init__(self, directed=True):
        self.directed = directed
        self.nodes = {}
    def add_node(self, nodename):
        if nodename not in self.nodes:
            self.nodes[nodename] = {}
    def add_edge(self, fromnode, tonode, weight=1, bidirectional=False):
        self.nodes[fromnode][tonode] = weight
        if (bidirectional or not self.directed) and fromnode != tonode:
            self.nodes[tonode][fromnode] = weight
    def copy(self):
        g = graph()
        g.directed = self.directed
        g.nodes = {}
        for k in self.nodes:
            g.nodes[k] = self.nodes[k].copy()
        return g
    def djikstra(self, src, dest):
        dist = {k:float('inf') for k in self.nodes}
        dist[src] = 0
        current = src
        visited = set()
        while dest not in visited:
            for node in self.nodes[current]:
                if node not in visited:
                    dist[node] = min(dist[node], 
                                     dist[current] + self.nodes[current][node])
            visited.add(current)
            cdist = float('inf')
            for k in dist:
                if k not in visited and dist[k] < cdist:
                    current = k
                    cdist = dist[current]
        return dist[dest]

def testcase(f):
    (N, Q) = [int(i) for i in f.readline().split()]
    horses = []
    for _ in range(N):
        horses.append(tuple(int(i) for i in f.readline().split()))
    dist = []
    for _ in range(N):
        dist.append([int(i) for i in f.readline().split()])
    g1 = graph()
    for i in range(N):
        g1.add_node(i)
    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1:
                g1.add_edge(i, j, dist[i][j])
    #print('A')
    g2 = graph()
    for i in range(N):
        g2.add_node(i)
    stack = []
    for src in range(N):
        stack.append(((src,), horses[src][0]))
    #print('B')
    while stack:
        (path, remaining) = stack.pop()
        for pd in g1.nodes[path[-1]]:
            if pd not in path and g1.nodes[path[-1]][pd] <= remaining:
                stack.append((path + (pd,), 
                              remaining - g1.nodes[path[-1]][pd]))
                if pd not in g2.nodes[path[0]] or \
                   g2.nodes[path[0]][pd] > (horses[path[0]][0] - stack[-1][1]):
                    g2.nodes[path[0]][pd] = horses[path[0]][0] - stack[-1][1]
    #print('C')
    for src in g2.nodes:
        for dst in g2.nodes[src]:
            g2.nodes[src][dst] /= horses[src][1]
    #print(g2.nodes)
    
    sols = []
    for _ in range(Q):
        (src, dst) = [int(i) for i in f.readline().split()]
        sols.append(g2.djikstra(src-1, dst-1))
    return ' '.join('{:0.7f}'.format(sol) for sol in sols)


cj = CodeJam(testcase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')
