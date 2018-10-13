#!/usr/bin/python

import sys, os

basename,ext = os.path.splitext(os.path.basename(sys.argv[0]))
basename= '-'.join([basename] + sys.argv[1:])
input = open(basename+'.in')
output = open(basename+'.out','w')

T = int(input.readline())

def solve():
    N = int(input.readline())
    naomi = map(float,input.readline().split())
    ken = map(float,input.readline().split())
    naomi.sort()
    ken.sort()
    print N, naomi, ken

    nn = naomi[:]
    kk = ken[:]
    old = 0
    while nn:
        k=0
        while k<len(kk) and kk[k]<nn[0]:
            k += 1
        if k==len(kk):
            kk.pop(0)
            nn.pop(0)
            old += 1
        else:
            kk.pop(k)
            nn.pop(0)

    score = 0
    while naomi:
        if ken[-1]>naomi[-1]:
            naomi.pop(0)
            ken.pop(-1)
        else:
            naomi.pop(-1)
            ken.pop(-1)
            score += 1    
    return score, old

for t in range(T):
    print >> output, "Case #%s: %s %s" % ((t+1,) + solve())
