import sys
from numpy import zeros
def floyd_wharsall(graph):
    n = len(graph)
    dist = zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i, j] = graph[i][j]
 
    for k in range(n):        
        for i in range(n):
            for j in range(n):
                if dist[i, k] != -1 and dist[k, j] != -1:
                    if dist[i, j] == -1 or dist[i, j] > dist[i, k] + dist[k, j]:
                        dist[i, j] = dist[i, k] + dist[k, j]
                        

    return dist
    
    
def solve(horses, distances, deliveries):
    distances = floyd_wharsall(distances)
    n = len(horses)
    times = zeros((n, n))
    
    for i in range(len(horses)):
        for j in range(len(horses)):
            if horses[i][0] >= distances[i, j] and distances[i, j] != -1:
                times[i, j] = distances[i, j] / horses[i][1]
            else:
                times[i, j] = -1
    
    min_times = floyd_wharsall(times)
    
    d_times = []
    for d in deliveries:
        d_times.append(min_times[d])
        
    return d_times

with open(sys.argv[1]) as infile:
    T = int(infile.readline())
    for i in range(1, T + 1):
        N, Q = [int(x) for x in infile.readline().split()]
        horses = []
        for _ in range(N):
            horses.append(tuple([int(x) for x in infile.readline().split()]))
            
        distances = []
        for _ in range(N):
            distances.append(tuple([int(x) for x in infile.readline().split()]))
        
        deliveries = []
        for _ in range(Q):
            deliveries.append(tuple([int(x) - 1 for x in infile.readline().split()]))
            
        print "Case #%d:" % i, ' '.join([str(x) for x in solve(horses, distances, deliveries)])