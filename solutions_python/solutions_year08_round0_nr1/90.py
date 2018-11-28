#!/usr/bin/python

N = int(raw_input())
for case in range(1, N + 1):
    S_range = range(int(raw_input()))
    S = dict([(raw_input(), x) for x in S_range])
    Q_range = range(int(raw_input()) - 1, -1, -1)
    Q = [S[raw_input()] for x in Q_range]
    S = map(lambda x: [None] * len(Q), S)
    for x in S_range:
        z = len(Q)
        for y in Q_range:
            if Q[y] == x:
                z = y
            S[x][y] = z
    n = 0
    if Q:
        s = reduce(lambda x, y: S[y][0] >= S[x][0] and y or x, S_range, 0)
        q = S[s][0]
        while q < len(Q):
            n += 1
            s = reduce(lambda x, y: S[y][q] >= S[x][q] and y or x, S_range, 0)
            q = S[s][q]
    print 'Case #%d:' % case, n
