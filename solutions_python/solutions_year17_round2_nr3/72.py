from collections import defaultdict
from heapq import heappop, heappush


def color(ndist, dist, hd, hv, s, v):
    for n in dist[v]:
        if dist[v][n] <= hd:
            if ndist[s][n] > ndist[s][v] + dist[v][n] / hv:
                ndist[s][n] = ndist[s][v] + dist[v][n] / hv
                color(ndist, dist, hd - dist[v][n], hv, s, n)
                

def new_dists(n, dist, horses):
    ndist = defaultdict(lambda: defaultdict(lambda: float('inf')))

    for i in range(n):
        ndist[i][i] = 0
        color(ndist, dist, horses[i][0], horses[i][1], i, i)
    
    return ndist

def dij(dist, s, target):
    dist[s][s] = 0
    heap = [(0, s)]
    marked = defaultdict(bool)
    while heap:
        d, v = heappop(heap)
        if v == target:
            return d
        if marked[v]:
            continue
        marked[v] = True
        dist[s][v] = d
        for n in dist[v]:
            nd = d + dist[v][n]
            heappush(heap, (nd, n))

for case in range(int(input())):
    n, q = map(int, input().split())
    horses = [tuple(map(int, input().split())) for _ in range(n)]
    dist = defaultdict(dict)
    for i in range(n):
        for j, d in enumerate(map(int, input().split())):
            if d != -1:
                dist[i][j] = d
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    ndist = new_dists(n, dist, horses)
    print('Case #%i:' % (case + 1), *(dij(ndist, a-1, b-1) for a,b in queries))
