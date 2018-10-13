from library import *
from itertools import permutations

def play(N,P,Q):
    P.sort()
    Q.sort()
    pi = 0
    qi = 0
    depth = 0
    mindepth = 0
    while pi < N and qi < N:
        if P[pi] < Q[qi]:
            depth += 1
            pi += 1
        else:
            depth -= 1
            if depth < mindepth:
                mindepth = depth
            qi += 1
    return -mindepth

def dplay(N,P,Q):
    P.sort()
    Q.sort()
    pi = 0
    qi = 0
    depth = 0
    maxdepth = 0
    while pi < N and qi < N:
        if P[pi] < Q[qi]:
            depth += 1
            if depth > maxdepth:
                maxdepth = depth
            pi += 1
        else:
            depth -= 1
            qi += 1
    return N-maxdepth

f = file('d.in2','r')
T = readint(f)
for case in range(1,T+1):
    N = readint(f)
    P = [float(x) for x in readstrs(f)]
    Q = [float(x) for x in readstrs(f)]
    ans = play(N,P,Q)
    dans = dplay(N,P,Q)
    print 'Case #%d: %d %d' % (case, dans, ans)
