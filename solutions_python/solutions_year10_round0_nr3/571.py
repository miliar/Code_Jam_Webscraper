#!/usr/bin/env python

from collections import deque

T = int(raw_input())
for tc in range(T):
    R,k,N = [int(rkn) for rkn in raw_input().split()]
    g = deque([int(gi) for gi in raw_input().split() ])
    income=0
    totgrps=len(g)

    for rounds in range(R):
        pc=k
        grps=0
        while 1 and grps < totgrps:
            pc-=g[0]
            if pc < 0:
                pc+=g[0]
                break
            g.append(g.popleft())
            grps+=1
        income+=(k-pc)
    print "Case #"+str(tc+1)+":", income
