from __future__ import division

def work(C,F,X):
    m = X/2
    if X<=C:
        return m
    K = int(X/C)
    ret = m
    for k in xrange(K):
        k = k + 1
        tmp = X/(2+k*F)
        for i in xrange(k):
            tmp += C/(2+i*F)
        ret = min(ret, tmp)
    return ret

with open('B.in','r') as f:
    T = int(f.readline())
    for t in xrange(T):
        ret = "Case #%d: " % (t+1)
        C,F,X = f.readline().split()
        C = float(C)
        F = float(F)
        X = float(X)
        value = work(C,F,X)
        ret += "%f" % value
        print ret


        
