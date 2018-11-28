from library import *
from math import ceil

def run(C,F,X):
    r = 2.
    if C >= X:
        return X/r
    k = int(ceil(X/C - r/F -1))
    k = max(k,0)
    s = 0
    for i in range(k):
        s += C/(r + i*F)
    return s + X/(r+k*F)

f = file('b.in2','r')
T = readint(f)
for case in range(1,T+1):
    C,F,X = [float(x) for x in readstrs(f)]
    ans = run(C,F,X)
    print 'Case #%d: %f' % (case, ans)
