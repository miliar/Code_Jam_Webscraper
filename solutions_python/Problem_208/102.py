#!/bin/python3
cities = {}
dists = {}


def calc(U, V, E, S):
    if U == V:
        return 0
    # elif E < 0:
    #     return -(10**12)
    else:
        dist = dists[U][U + 1]
        if dist <= E:
            cont = calc(U + 1, V, E - dist, S) + dist / S
            chan = calc(U + 1, V, cities[U][0] - dist, cities[U][1]) + dist / cities[U][1]
            return min(cont, chan)
        else:
            chan = calc(U + 1, V, cities[U][0] - dist, cities[U][1]) + dist / cities[U][1]
            return chan


T = int(input().strip())
for test in range(T):
    N, Q = [int(x) for x in input().split()]
    # read map
    cities = {}
    for i in range(N):
        E, S = [int(x) for x in input().split()]
        cities[i] = (E, S)
    dists = {}
    for i in range(N):
        dist = [int(x) for x in input().split()]
        dists[i] = dist
    # read queries
    for i in range(Q):
        U, V = [int(x) for x in input().split()]
        U -= 1
        V -= 1
        ans = calc(U, V, cities[U][0], cities[U][1])
        print('Case #%d: %f' % ((test + 1), ans))
