# Python program for implementation of Ford Fulkerson algorithm

from collections import defaultdict


# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


f = open('in', 'r')
fout = open('out', 'w')
t = int(f.readline())
for casenum in range(1, t + 1):
    print "casenum", casenum
    def can(k, n):
        n = n[0]
        incr = n
        while True:
            # print k, n
            if n > 2 * k:
                break
            bounds = [0.9 * n, 1.1 * n]
            # print bounds
            if bounds[0] <= k <= bounds[1]:
                # print "succ"
                return True
            n += incr
        return False

    def cann(n, k1, k2):
        # print "casenum", casenum
        # print n
        # print k1, k2
        incr = n
        n1 = n[0]
        n2 = n[1]
        while True:
            if n1 > 2 * k1 and n2 > 2 * k2:
                break
            bounds1 = [0.9 * n1, 1.1 * n1]
            bounds2 = [0.9 * n2, 1.1 * n2]
            if bounds1[0] <= k1 <= bounds1[1] and bounds2[0] <= k2 <= bounds2[1]:
                return True
            n1 += incr[0]
            n2 += incr[1]

    n_size, p_size = f.readline().split()
    n_size = int(n_size)
    p_size = int(p_size)
    n = f.readline().split()
    n = [int(k) for k in n]
    p = []
    for i in range(n_size):
        line = f.readline().split()
        line = [int(k) for k in line]
        p.append(line)

    # if casenum == 9:
    #     break
    # if casenum != 8:
    #     continue


    # print n_size, p_size
    # print n
    # for k in p:
    #     print k


    if n_size == 1:
        tot = 0
        for k in p[0]:
            if can(k, n):
                tot += 1
        # print tot
    else:

        d = dict()
        for i in range(p_size):
            for j in range(p_size):
                if i not in d:
                    d[i] = []
                if cann(n, p[0][i], p[1][j]):
                    d[i].append(j)

        # Create a graph given in the above diagram
        sz =  2 * p_size + 2
        m = [[0] * (sz) for i in range(sz)]
        # 1...psize = from
        # psize+1 ... 2psize + 1

        # graph = [[0, 16, 13, 0, 0, 0],
        #          [0, 0, 10, 12, 0, 0],
        #          [0, 4, 0, 0, 14, 0],
        #          [0, 0, 9, 0, 0, 20],
        #          [0, 0, 0, 7, 0, 4],
        #          [0, 0, 0, 0, 0, 0]]
        #
        # g = Graph(graph)


        # print d

        source = 0
        sink = sz-1
        for k in d:
            # print source, k+1
            m[source][k+1] = 1
            for next in d[k]:
                m[k+1][next+1+p_size] = 1

        for i in range(p_size+1, sink):
            m[i][sink] = 1

        # for k in m:
        #     print k

        g = Graph(m)
        tot = g.FordFulkerson(source, sink)

        # for k in d:
        #     print k, d[k]
        # tot = 0
        #
        # print d
        #
        # toremove = 123902348
        # while toremove is not None:
        #     toremove = None
        #     for k in d:
        #         if len(d[k]) == 1:
        #             tot += 1
        #             toremove = d[k][0]
        #             for k in d:
        #                 if toremove in d[k]:
        #                     d[k].remove(toremove)
        #         break
        #
        # # print d
        # # print ""
    # print tot



    fout.write("Case #{}: {}\n".format(casenum, tot))

print "done"