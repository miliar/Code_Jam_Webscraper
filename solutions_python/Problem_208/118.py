
class Horse:

    def __init__(self, dist, speed):
        self.speed = speed
        self.dist = dist

# O(N^2) * O(Djikstra)
def findPath(u, v, graph, horses):
    N = len(horses)
    finalTime = dict()
    minTime = {i: float("inf") for i in range(N)}
    minTime[u] = 0
    while minTime:
        # pop off heap
        nextHorse = min(minTime, key=lambda x:minTime[x])
        finalTime[nextHorse] = minTime[nextHorse]
        del minTime[nextHorse]

        # run Djikstra
        distances = Djikstra(graph, nextHorse, N)

        # update
        for i in range(N):
            if i in minTime.keys() and distances[i] <= horses[nextHorse].dist:
                minTime[i] = min(minTime[i], finalTime[nextHorse] + distances[i]/horses[nextHorse].speed)
        
    return finalTime[v]

# O(N^2)
def Djikstra(graph, start, N):
    finalDist = dict()
    dist = {i: float("inf") for i in range(N)}
    dist[start] = 0

    while dist:
        # pop of "heap"
        node = min(dist, key=lambda x:dist[x])
        finalDist[node] = dist[node]
        del dist[node]

        if finalDist[node] == float("inf"):
            continue

        # Update future nodes
        for i in range(N):
            if i in dist.keys() and graph[node][i] > -1:
                dist[i] = min(dist[i], finalDist[node] + graph[node][i])

    return finalDist
        
# O(N^5)
def solve():
    N, Q = [int(x) for x in input().split()]
    horses = list()
    for i in range(N):
        E, S = [int(x) for x in input().split()]
        horses.append(Horse(E, S))
    graph = [ [ int(x) for x in input().split()] for i in range(N)]
    ans = list()
    for _ in range(Q):
        u, v = [int(x) - 1 for x in input().split()]
        ans.append(findPath(u, v, graph, horses))

    return " ".join([str(x) for x in ans])

def findPathFast(u, v, dist, horses):
    N = len(horses)
    finalTime = dict()
    minTime = {i: float("inf") for i in range(N)}
    minTime[u] = 0
    while minTime:
        # pop off heap
        nextHorse = min(minTime, key=lambda x:minTime[x])
        finalTime[nextHorse] = minTime[nextHorse]
        del minTime[nextHorse]

        # update
        for i in range(N):
            if i in minTime.keys() and dist[nextHorse][i] <= horses[nextHorse].dist:
                minTime[i] = min(minTime[i], finalTime[nextHorse] + dist[nextHorse][i]/horses[nextHorse].speed)
        
    return finalTime[v]

def FloydWarshall(graph, N):
    dist = [[0 for i in range(N)] for j in range(N)]
    
    for i in range(N):
        for j in range(N):
            dist[i][j] = graph[i][j]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# O(N^3)
def solveFast():
    N, Q = [int(x) for x in input().split()]
    horses = list()
    for i in range(N):
        E, S = [int(x) for x in input().split()]
        horses.append(Horse(E, S))
    graph = [ [ int(x) for x in input().split()] for i in range(N)]
    ans = list()

    dist = FloydWarshall(graph, N)
    
    
    for _ in range(Q):
        u, v = [int(x) - 1 for x in input().split()]
        ans.append(findPath(u, v, graph, horses))

    return " ".join([str(x) for x in ans])
    

t = int(input())
for i in range(t):
    ans = solveFast()
    print("Case #%d: %s" % (i + 1, ans))
