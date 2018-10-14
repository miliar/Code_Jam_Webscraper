def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

import sys
sys.setrecursionlimit(1000000)
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments.
    to clear the internal DP dict: use f.clear() """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):  
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

def testcase(cas=-1):
    N, Q = readvals() 
    E, S = zip( *[readvals(float) for _ in xrange(N)] ) 
    D = [ readvals() for _ in xrange(N) ] 
    UV = [readvals() for _ in xrange(Q)] # small case: Q = 1
    
    @memoize
    def mintime(i): 
        if i==N-1: return 0 
        dist = 0.0
        res = 1e100
        for j in xrange(i+1, N): 
            dist += D[j-1][j]
            if dist > E[i]: break 
            res = min(res, dist / S[i] + mintime(j))
        return res 
    res = mintime(0)
    print 'Case #%d: %.7f' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
