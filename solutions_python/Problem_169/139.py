
#from itertools import 
#from collections import 
import sys
sys.setrecursionlimit(10000)

def merge(sources):
    R = 0
    C = 0
    for r,c in sources:
        C = (R*C + r*c)/(R+r)
        R += r
    return R,C

def solve_with_hot(V, X, hot):
    sources = [s for s in hot if s[1]==X]
    if not sources:
        return "IMPOSSIBLE"

    source = merge(sources)
    return V/source[0]

def solve_with_hot_mild(V, X, hot, cold, mild):
    if mild[1] == X:
        return V/mild[0]

    t1 = V*(X-cold[1])/(mild[0]*(mild[1]-cold[1]))
    t2 = (V-mild[0]*t1)/cold[0]

    return t1+t2

def solve(V, X, S):
    hot = [s for s in S if s[1]>=X]
    cold = [s for s in S if s[1]<X]

    if not hot:
        return "IMPOSSIBLE"

    if not cold:
        return solve_with_hot(V, X, hot)

    hot = merge(hot)
    cold = merge(cold)
    mild = merge([hot, cold])

    if mild[1] >= X:
        return solve_with_hot_mild(V, X, hot, cold, mild)

    t1 = V*(X-mild[1])/(hot[0]*(hot[1]-mild[1]))
    t2 = (V-hot[0]*t1)/mild[0]

    return t1+t2


def parse_args():
    N, V, X = map(float, raw_input().split())
    S = [map(float, raw_input().split()) for _ in xrange(int(N))]
    return [V, X, S]

T = int(raw_input())
for t in xrange(1, T+1):
    print "Case #%d: %s" % (t, solve(*parse_args()))
