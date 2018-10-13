T = int(input())


from heapq import heappop, heappush


def floyd_warshall(weight):
    """All pairs shortest paths by Floyd-Warshall
    :param weight: edge weight matrix
    :modifies: weight matrix to contain distances in graph
    :returns: true if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    V = range(len(weight))
    for k in V:
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v],
                                   weight[u][k] + weight[k][v])
    for v in V:
        if weight[v][v] < 0:      # cycle négatif détecté
            return True
    return False

def algo(N, Q, cities, graph, routes):
    for i in range(N):
        for j in range(N):
            if graph[i][j] < 0:
                graph[i][j] = float('inf')
    dist = [x.copy() for x in graph] # deepcopy
    floyd_warshall(dist)

    res = [[0]*N for _ in range(N)]

    for i in range(N):
        EI, SI = cities[i]
        for j in range(N):
            if dist[i][j] <= EI:
                res[i][j] = dist[i][j]/SI
            else:
                res[i][j] = float('inf')
    floyd_warshall(res)

    result = ""
    for r in routes:
        result += str(res[r[0]-1][r[1]-1]) + " "
    return result.strip()



for i in range(T):
    N, Q = [int(x) for x in input().split(' ')]
    cities = [[int(x) for x in input().split(' ')] for _ in range(N)]
    graph = [[int(x) for x in input().split(' ')] for _ in range(N)]
    routes = [[int(x) for x in input().split(' ')] for _ in range(Q)]
    print("Case #%d: %s" % (i+1, algo(N,Q,cities,graph,routes)))
