# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=433101#s=p2
'''

import sys

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

T = int(lin())

for casenum in range(T):
    (R, k, N) = ints()
    gs = ints()
    assert len(gs)==N

    end = 0
    size = [0]*N
    ends = [0]*N
    for i in range(N):
        if i>0: size[i] = size[i-1] - gs[i-1]
        else:   size[i] = gs[0]
        if end+1==i:
            size[i] = gs[i]
            end += 1
        while (end+1)%N != i and size[i] + gs[(end+1)%N] <= k:
            end = (end+1)%N
            size[i] += gs[end]

        ends[i] = end

#     print size
#     print ends

    seq = []
    i=0
    head = []
    rho  = []
    while True:
        if seq.count(i):
            head = seq[:seq.index(i)]
            rho  = seq[seq.index(i):]
            break
        seq.append(i)
        i = (ends[i] + 1)%N

    #print head, rho

    ans = 0
    for i in range(len(head)):
        if i<R:
            ans += size[head[i]]
        else:
            break

    R -= len(head)
    if R>0:
        rhosum = sum(size[r] for r in rho)
        times = R/len(rho)
        ans += rhosum*times
        R -= times*len(rho)

    for i in range(R):
        ans += size[rho[i]]

    print "Case #%d: %s" % (casenum+1, ans)
