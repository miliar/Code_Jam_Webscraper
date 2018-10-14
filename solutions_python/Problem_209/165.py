import sys
sys.setrecursionlimit(1000000)
def memoize(f):
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):  
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


def readvals(typ=int):
    return map(typ, raw_input().split())

def readval(typ=int):
    return typ( raw_input() )

from math import pi 
import numpy as np 

def testcase(case=-1):
    N, K = readvals() 
    RH = sorted([tuple(readvals()) for _ in xrange(N)], reverse=True)
    R, H = zip(*RH)
    
    @memoize
    def f(i,k): 
        if k <= 0: return 0
        if N-i < k: return -1e1000
        return max( f(i+1, k), f(i+1,k-1)+2*R[i]*H[i] )

    result = 0
    for j in xrange(N-K+1): 
        s = R[j]**2 + R[j]*2*H[j] + f(j+1,K-1)
        result = max(s, result) 
    result *= pi 
    print 'Case #%d: %.9f' % (case, result)

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
