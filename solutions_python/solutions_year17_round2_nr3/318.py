#! /bin/python

from sys import stdin
from math import inf

T = int(stdin.readline())


for t in range(T):
    [N, Q] = [int(x) for x in stdin.readline().split()]
    cities = []
    for _ in range(N):
        [e, s] = stdin.readline().split()
        cities.append((int(e), int(s)))

    G = []
    for _ in range(N):
        G.append([int(x) for x in stdin.readline().split()])

    for _ in range(Q):
        [u, v] = [int(x) for x in stdin.readline().split()]

    # Small case
    minTime = [inf]*N
    minTime[N-1] = 0
    for city in range(N-2, -1, -1):
        times = []
        d = 0
        for dest in range(city+1, N):
            (e, s) = cities[city]
            # d = sum(G[x][x+1] for x in range(city, dest))
            d += G[dest-1][dest]
            if e >= d:
                times.append(minTime[dest] + d/s)
            else:
                break
        minTime[city] = min(times)

    print("Case #{}: {}".format(t+1, minTime[0]))
