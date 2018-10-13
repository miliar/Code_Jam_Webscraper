#!/usr/bin/env python

from sys import stdin


N = int(stdin.readline())

for i in range(1,1+N):
    wds = stdin.readline().split()
    N = int(wds[0])
    S = int(wds[1])
    p = int(wds[2])

    T = [ int(j) for j in wds[3:]]

    ok = 0
    yobi = 0
    for t in T:
        score = t / 3
        amari = t % 3
        if amari != 0: score += 1
        if score + 1 < p: continue
        if score >= p:
            ok += 1
            continue
        if amari != 1 and t != 0: yobi += 1
        pass

    #print ok, yobi, S

    ok += min([yobi, S])

    print "Case #%d: %d" % (i, ok)
