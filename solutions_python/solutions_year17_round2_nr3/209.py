import sys
import numpy as np

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr


def floydWarshall(graph):
    nodes = graph.keys()
    distance = {}

    for n in nodes:
        distance[n] = {}
        for k in nodes:
            distance[n][k] = graph[n][k]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[i][j] = min (distance[i][j], distance[i][k] + distance[k][j])
    return distance

INF=2000000000
T = int(fin.readline())

for case in range(T):
    l = fin.readline()
    N = int(l.split()[0])
    Q = int(l.split()[1])
    
    E = np.zeros(N, dtype=int)
    S = np.zeros(N, dtype=int)
    for h in range(N):
        l = fin.readline()
        E[h] = int(l.split()[0])
        S[h] = int(l.split()[1])
    
    graph = {}
    C = np.zeros((N,N), dtype=int)
    D = np.zeros((N), dtype=int)
    for c in range(N):
        l = fin.readline()
        ds = list(map(int, l.split()))
        for d in range(N):
            C[c,d] = INF if ds[d]<0 else ds[d]
            graph.setdefault(c,{})[d] = C[c,d]
        if c<N-1:
            D[c] = C[c,c+1]
    dist = floydWarshall(graph)
    
    for q in range(Q):
        l = fin.readline()

    TD = np.zeros(N)
    for h in range(N-2,-1,-1):
        TD[h] = min( TD[j]+(dist[h][j]/S[h]) for j in range(h+1, N) if dist[h][j]<=E[h] )
    
    fout.write("Case #%i: %.7f\n" % (case+1, TD[0]))

