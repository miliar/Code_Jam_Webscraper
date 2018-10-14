#!/usr/bin/env python

from sys import stdin

T = int(stdin.readline())

for t in range(T):
    ## input
    wds = stdin.readline().split()
    N = int(wds[0])

    d_l = []
    for i in range(N):
        wds = stdin.readline().split()
        d_l.append((int(wds[0]), int(wds[1])))
        pass

    wds = stdin.readline().split()
    D = int(wds[0])

    ok = [(d_l[0][0], d_l[0][0])]
    kita = 1
    ret = False
    while len(ok) > 0:
        #print ok
        now = ok[0]
        ok = ok[1:]
        if now[0] + now[1] >= D:
            ret = True
            break
        if kita >= len(d_l): continue
        for turu in d_l[kita:]:
            if now[0] + now[1] < turu[0]: break
            ok.append((turu[0], min(turu[0]-now[0], turu[1])))
            kita += 1
            pass
        pass

    ## output
    print "Case #%d:" % (t+1),
    if ret:
        print "YES"
    else:
        print "NO"
