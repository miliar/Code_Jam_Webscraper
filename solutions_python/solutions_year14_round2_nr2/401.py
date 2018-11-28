"""
def sol_dp_single(E, R, N, vals, dp, i, v):
    if i==N:
        return 0
    if (i, v) in dp:
        return dp[(i, v)]
    
    curr = -1
    for spent in range(v+1):
        curr = max(curr, vals[i]*spent + sol_dp_single(E, R, N, vals, dp, i+1, min(E, v-spent+R)))
    dp[(i, v)] = curr
    return curr

def sol_dp(E, R, N, vals):
    dp = {}
    return sol_dp_single(E, R, N, vals, dp, 0, E)
"""
def brute(A, B, K):
    p = 0
    for i in xrange(A):
        for j in xrange(B):
            if i&j < K:
                p+=1
    return p

import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    A, B, K = map(int, sys.stdin.readline().split())
    #print "wynik brute:", sol_dp(E, R, N, vals)
    print "Case #"+str(case)+": "+str(brute(A, B, K))
