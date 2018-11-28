from __future__ import division
import sys, re
readline = sys.stdin.readline

def best(i,j,torel,mem=None):
    if mem is None:
        mem = {}
    if (i,j) in mem:
        return mem[i,j]
    if not torel:
        mem[i,j] = 0
        return 0
    mem[i,j] = (j - i - 1 +
                min(best(i,rel,torel[:n],mem) +
                    best(rel+1,j,torel[n+1:],mem)
                    for (n,rel) in enumerate(torel)))
    return mem[i,j]

N = int(readline())
for case in range(1, 1 + N):
    P,Q = [int(word) for word in readline().split()]
    torel=[int(word)-1 for word in readline().split()]
    res = best(0,P,torel)
    print "Case #%s: %s"%(case,res)
