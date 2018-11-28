#!/usr/bin/env python3
import sys
from collections import defaultdict
def ri():
    return map(int, sys.stdin.readline().split())


T = int(input())

for i in range(T):
    AC, AJ = ri()
    CD = []
    JK = []
    tCbaby = 0
    tJbaby = 0
    for ii in range(AC):
        a, b = ri()
        tJbaby += b - a
        CD.append((a,b,0))
    for ii in range(AJ):
        a, b = ri()
        tCbaby += b - a
        JK.append((a, b, 1))
    CDJK = CD + JK
    CDJK.sort()
    SCDi = []
    SJKi = []
    for ii in range(AC+AJ):
        if CDJK[ii][2] == CDJK[(ii+1)%(AC+AJ)][2]:
            if CDJK[ii][2] == 0:
                SCDi.append(ii)
            else:
                SJKi.append(ii)
    SCDi.sort(key=lambda e: (CDJK[(e+1)%(AC+AJ)][0] - CDJK[e][1]+1440)%1440)
    SJKi.sort(key=lambda e: (CDJK[(e+1)%(AC+AJ)][0] - CDJK[e][1]+1440)%1440)
    ans = 0
    for ii in range(AC+AJ):
        if CDJK[ii][2] == CDJK[(ii+1)%(AC+AJ)][2]:
            ans += 2
        else:
            ans += 1
    #print("ans", ans)

    for ii in SCDi:
        e1 = CDJK[ii]
        e2 = CDJK[(ii+1)%(AC+AJ)]
        tt = (e2[0] - e1[1] + 1440)%1440
        #print("tJbaby",ii, e1,e2, tt, tJbaby)
        if tJbaby + tt <= 720:
            tJbaby += tt
            ans -= 2
        else:
            break
    for ii in SJKi:
        e1 = CDJK[ii]
        e2 = CDJK[(ii+1)%(AC+AJ)]
        tt = (e2[0] - e1[1] + 1440)%1440
        #print("tCbaby", ii, e1,e2, tt, tCbaby)
        if tCbaby + tt <= 720:
            tCbaby += tt
            ans -= 2
        else:
            break



    print("Case #%d:"%(i+1), ans)
