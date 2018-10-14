#!/usr/bin/env python

def solve():
    nse = int(raw_input())
    ses = []
    for i in range(nse):
        ses.append(raw_input())
    nq = int(raw_input())
    MAX = nq+1
    qs = []
    for i in range(nq):
        qn = raw_input()
        qs.append(ses.index(qn))
    s = {}
    for i in range(nse):
        s[0,i] = 0
    for i in range(1, nq+1):
        for j in range(nse):
            s[i,j] = MAX
            for k in range(nse):
                if k <> qs[i-1]:
                    v=s[i-1, k]
                    if j<>k:
                        v+=1
                    if v < s[i,j]:
                        s[i,j] = v
    v = min(s[nq,j] for j in range(nse))
    return v

n = int(raw_input())
for i in range(n):
    print "Case #%d: %d"%(i+1, solve())

