#!/usr/bin/env python3

from queue import PriorityQueue


def dijkstra(graph, start, E):
    sp = [float('inf') for i in range(len(graph))]
    Q = PriorityQueue()
    sp[start] = 0
    Q.put((sp[start], start))
    while not Q.empty():
        old_sp, v = Q.get()
        if old_sp > sp[v]:
            continue
        for u in range(len(graph)):
            if graph[v][u] != -1:
                new_dist = graph[v][u] + sp[v]
                if new_dist <= E and new_dist < sp[u]:
                    sp[u] = new_dist
                    Q.put((sp[u], u))
    return sp

T = int(input())
for case in range(1, T + 1):
    N, Q = map(int, input().split())
    horses = tuple(tuple(map(int, input().split())) for i in range(N))
    adj = tuple(tuple(map(int, input().split())) for i in range(N))
    query = tuple(tuple(map(int, input().split())) for i in range(Q))
    adj_t = list()
    for h in range(N):
        sp = dijkstra(adj, h, horses[h][0])
        for i in range(len(sp)):
            sp[i] /= horses[h][1]
        adj_t.append(sp)
    answers = []
    for u, v in query:
        sp = dijkstra(adj_t, u - 1, float('inf'))
        answers.append(str(sp[v - 1]))
    answer = ' '.join(answers)
    print("Case #", case, ": ", answer, sep="")
