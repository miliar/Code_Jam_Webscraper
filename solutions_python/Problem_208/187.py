# Pony Express

import heapq

def solve(n, e, s, d, u, v):
    t = 0
    q = [(0, u, u, es[0][0])]
    visited = {}
    while len(q) > 0:
        (t, c, h, r) = heapq.heappop(q)
        if c == v:
            return t
        if visited.get((c, h), False):
            continue
        visited[(c, h)] = True
        for i in range(n):
            if d[c][i] >= 0 and r >= d[c][i]:
                heapq.heappush(q, (t + d[c][i] / s[h], i, h, r - d[c][i]))
        for i in range(n):
            if d[c][i] >= 0:
                heapq.heappush(q, (t + d[c][i] / s[c], i, c, e[c] - d[c][i]))
    return -1

cases = int(raw_input())
for case in range(1, cases + 1):
    (n, q) = map(int, raw_input().split(' '))
    es     = [map(int, raw_input().split(' ')) for x in range(n)]
    (e, s) = ([p[0] for p in es], [p[1] for p in es])
    d      = [map(float, raw_input().split(' ')) for x in range(n)]
    uvs    = [map(int, raw_input().split(' ')) for x in range(q)]
    print "Case #" + str(case) + ": " + ' '.join(map(str, [solve(n, e, s, d, u - 1, v - 1) for (u, v) in uvs]))
