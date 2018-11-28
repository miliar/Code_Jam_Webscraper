# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(1, T + 1):
    nc, nj = map(int, rl().split())
    print >> sys.stderr, tcase, nc, nj
    C = [map(int, rl().split()) for i in range(nc)]
    CS = sum([c[1] - c[0] for c in C])
    C = [['c', a, b] for a, b in C]
    J = [map(int, rl().split()) for i in range(nj)]
    JS = sum([j[1] - j[0] for j in J])
    J = [['j', a, b] for a, b in J]
    S = C + J
    S.sort(key=lambda x: (x[1], x[2]))
    print >> sys.stderr, S
    remain = {'c': 720 - CS, 'j': 720 - JS}
    while True:
        if len(S) == 1:
            break
        SS = []
        l = S[0]
        for i in range(1, len(S)):
            if S[i][0] == l[0] and remain[l[0]] >= (S[i][1] - l[2]):
                remain[l[0]] -= (S[i][1] - l[2])
                l[2] = S[i][2]
            else:
                SS.append(l)
                l = S[i]
        SS.append(l)
        if S == SS:
            break
        S = SS
    if S[0][0] ==  S[-1][0]:
        if remain[S[0][0]] >= (S[0][1] + 1440 - S[-1][2]):
            S.pop()
    print >> sys.stderr, S
    cnts = len(S)
    cnts += sum([1 for i in range(len(S)) if S[i - 1][0] == S[i][0]])
    print 'Case #%d: %s' % (tcase, cnts)
