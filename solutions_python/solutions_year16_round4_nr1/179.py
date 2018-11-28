import math


T = int(input())

op = {
    'S': 'PS',
    'P': 'PR',
    'R': 'RS'
}

def solve(n, r, p, s):
    if n == 0:
        if r: return 'R'
        if p: return 'P'
        if s: return 'S'
    s_ = 2**(n-1) - r
    r_ = 2**(n-1) - p
    p_ = 2**(n-1) - s
    if s_ < 0 or r_ < 0 or p_ < 0:
        return 'IMPOSSIBLE'
    result = solve(n-1, r_, p_, s_)
    if result == 'IMPOSSIBLE':
        return result
    return ''.join(map(lambda x:op[x], result))
from collections import Counter
memo = {
}
def g(n, w):
    if n == 0:
        return w
    if memo.get((n,w)):
        return memo.get((n,w))
    a,b = op[w]
    t1 = g(n-1, a)
    t2 = g(n-1, b)
    
    if t1 < t2:
        ret = t1 + t2
    else:
        ret = t2 + t1
    memo[(n, w)] = ret
    return ret
    
#print(g(3, 'P'))

def solve2(N, R, P, S):
    for w in ['R','P','S']:
        ret = g(N, w)
        c = Counter(ret)
        if c['R'] == R and c['P'] == P and c['S'] == S:
            return ret
    return "IMPOSSIBLE"
for t in range(1, T+1):
    N,R,P,S = map(int,input().split())
    print("Case #%d: %s" % (t, solve2(N, R, P, S)))