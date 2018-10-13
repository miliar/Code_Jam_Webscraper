#!/usr/bin/python3

import sys

def case():
    N = int(sys.stdin.readline())
    naomi = sorted([float(x) for x in sys.stdin.readline().split()], key = lambda x: -x)
    ken = sorted([float(x) for x in sys.stdin.readline().split()], key = lambda x: -x)
    i = j = N-1
    win = 0
    while i >= 0:
        if naomi[i] > ken[j]:
            j -= 1
            win += 1
        i -= 1
    j = 0
    owin = 0
    for i in range(N):
        if naomi[i] < ken[j]:
            j += 1
        else:
            owin += 1
    return "%s %s" % (win, owin)



T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

