#!/usr/bin/python3
import math
t = int(input())

for it in range(1, t+1) :
    NA, NB = [int(i) for i in input().split()]
    N = NA + NB
    C = []
    for i in range(N):
        b, e = [int(i) for i in input().split()]
        w = int(i >= NA)
        C.append((b, e, w))
    C = sorted(C)
    b0 = C[0][0]
    C = [(b-b0, e-b0, w) for (b, e, w) in C]
    if C[0][2] == 1: C = [(b, e, 1-w) for (b, e, w) in C]
    assert C[0][2] == 0 and C[0][0] == 0
    C.append((24*60, 24*60, 0))
    t = 0
    w = 0
    treq = [0, 0]
    tany = 0
    tadd = [[], []]
    #tfree = [[], []]
    tfree = [0, 0]
    x = 0
    #print("NA, NB:", NA, NB, N)
    #print("C:", C)
    for i in range(N+1):
        b, e, cw = C[i]
        assert t <= b
        if cw != w:
            tany += b - t
            x += 1
            w = cw
        else:
            tadd[1-w].append(b - t)
            tfree[w]+= (b - t)
        treq[w] += e - b
        t = e
    tadd = [sorted(ta, key = lambda t: -t) for ta in tadd]
    #print("treq:", treq)
    #print("tadd:", tadd)
    #print("tany:", tany)
    ans = 9999
    #if 1:
        #w = 0 if treq[0]+tfree[0] < treq[1]+tfree[1] else 1
    for w in [0, 1]:
        if treq[w] + tfree[w] > 720: continue
        xx = 0
        tt = treq[w] + tfree[w] + tany
        ii = 0
        while tt < 720 and ii < len(tadd[w]):
            tt += tadd[w][ii]
            ii += 1
            xx += 2
        ans = min(ans, x+xx)
        #assert tt >= 720
    print("Case #%d:"%it, ans)
