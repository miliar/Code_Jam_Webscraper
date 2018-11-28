'''
Created on 21 maj 2011
Hackyhack
@author: rickard
'''
import os,sys

def rpi(results):
    N = len(results[0])
    matches = [len(x.replace('.','')) for x in results]
    wp = [x.count('1') / float(matches[i]) for i,x in enumerate(results)]
    owp = []
    for i,t in enumerate(results):
        o = 0.0; ot = 0.0
        for j,c in enumerate(t):
            if c != '.':
                o1 = []
                for k,cc in enumerate(results[j]):
                    if cc == '.' or k == i: continue
                    o1.append(int(cc))
                o += sum(o1) / float(len(o1)); ot += 1
        if ot: owp.append(o / ot)
    oowp = []
    for i,t in enumerate(results):
        oowp.append(sum(owp[j] for j,x in enumerate(t) if x != '.') / float(matches[i]))
    return [.25*wp[i] + .5*owp[i] + .25*oowp[i] for i in range(N)]

count = int(sys.stdin.readline())
for c in range(count):
    n = int(sys.stdin.readline())
    l = [sys.stdin.readline().strip() for _ in range(int(n))]
    print "Case #%d:" % (c+1)
    print '\n'.join(map(str,rpi(l)))