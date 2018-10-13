# encoding: UTF-8
#Google Code Jam 2017 Round1B
#Problem C

import collections
import itertools
import sys

from priodict import priorityDictionary

class gcj:
    identity = lambda x: x

    @classmethod
    def _read_line_raw(cls):
        line = in_file.readline()
        if not line:
            raise EOFError()
        return line.rstrip('\r\n')

    @classmethod
    # read single character
    def token(cls, conv=identity):
        line = cls._read_line_raw()
        return conv(line)

    @classmethod
    # read multiple single characters splitted by sep
    def tokens(cls, conv=identity, sep = ' '):
        line = cls._read_line_raw()
        return [conv(i) for i in line.split(sep)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return('Case #{}: '.format(cls.current_case))

def Dijkstra(G,start,end=None):

    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0
    
    for v in Q:
        D[v] = Q[v]
        if v == end: break
        
        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v
    
    return (D,P)
            
def shortestPath(G,start,end):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    D,P = Dijkstra(G,start,end)
    Path = []
    while 1:
        Path.append(end)
        if end == start: break
        end = P[end]
    Path.reverse()
    return Path


def solve():
    N,Q = gcj.tokens(int)
    horse = []
    dist = []
    for _ in range(N):
        horse.append(gcj.tokens(int))
    for _ in range(N):
        dist.append(gcj.tokens(int))
    destin = []
    for _ in range(Q):
        destin.append(gcj.tokens(int))

    inf = float('inf')
    # graph = [[갈수있는점],[거리]]*N
    graph = {}

    for i in range(N):
        graph[i] = {}
        maxd = horse[i][0]
        sp = horse[i][1]
        queue = list(range(N))
        curr = i
        d = 0
        time = 0
        for j in range(i+1,N):
            nxt = j
            d += dist[curr][nxt]
            if d>maxd:
                break
            time += dist[curr][nxt]/sp
            curr = nxt
            if curr in graph[i].keys():
                graph[i][curr] = min(graph[i][curr],time)
            else:
                graph[i][curr] = time
    print(graph)
    ans = []
    for i,v in enumerate(destin):
        x = Dijkstra(graph, v[0]-1)
        res = x[v[0]-1][v[1]-1]
        print(res)
        ans.append(str(res))
    return(''.join(ans))


def main():
    sys.setrecursionlimit(9999)
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        solution = solve()
        out_file.write(case+solution+"\n")
        print(case+solution)
        sys.stdout.flush()

problem_name = 'C-small-attempt1'
in_file = open(problem_name+'.in',"r")
out_file = open(problem_name+'.out', "w")
main()
in_file.close()
out_file.close()