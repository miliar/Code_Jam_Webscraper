import math
from queue import PriorityQueue

def modifyGraph(graph, horses):
    newGraph = []
    for i in range(len(graph)):
        newGraph.append([math.inf] * len(graph))
    for (i, startCity) in enumerate(graph):
        (e, s) = horses[i]
        queue_cities = [(city, dist) for (city, dist) in enumerate(startCity) if dist != -1]
        while len(queue_cities) > 0:
            (city, dist) = queue_cities.pop(0)
            if dist <= e:
                newGraph[i][city] = min(newGraph[i][city], dist/s)
                queue_cities += [(c, d + dist) for (c, d) in enumerate(graph[city]) if d != -1]
    return newGraph

def dikstra(graph, start, end):
    citiesWithMinDist = set([start])

    queue = PriorityQueue()
    for (city, dist) in enumerate(graph[start]):
        queue.put((dist, city))

    while True:
        (dist, city) = queue.get()
        if city in citiesWithMinDist:
            continue
        citiesWithMinDist.add(city)
        if city == end:
            return dist
        for (nextCity, nextDist) in enumerate(graph[city]):
            queue.put((dist + nextDist, nextCity))

t = int(input())
for i in range(1, t+1):
    line = input()
    n = int(line.split(" ")[0])
    q = int(line.split(" ")[1])
    horses = []
    for j in range(n):
        line = input()
        e = int(line.split(" ")[0])
        s = int(line.split(" ")[1])
        horses.append((e, s))

    graph = []
    for j in range(n):
        line = input()
        graph.append([int(elem) for elem in line.split(" ")])

    newGraph = modifyGraph(graph, horses)
    # print(graph)
    # print()
    # print(newGraph)
    minTimes = []
    for j in range(q):
        line = input()
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        minTimes.append(dikstra(newGraph, u-1, v-1))

    print("Case #{}:".format(i), ' '.join((str(elem) for elem in minTimes)))