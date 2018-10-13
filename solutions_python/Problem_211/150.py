#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import numpy.linalg as linalg


def solve_small(N, K, U, Ps):
    
    
    A = [[1.0]*(N-1) for i in range(N-1)]
    for i in range(N-1):
        A[i][i] = 2.0
    B = [U + Ps[N-1] - Ps[i] for i in range(N-1)]
    a = np.array(A)
    b = np.array(B)
    x = linalg.solve(a,b)
    print U, Ps
    print a, b, x, U - sum(x)
    prod = U + Ps[N-1] - sum(x)
    for i in range(N-1):
        prod *= x[i] + Ps[i]
    return prod

def solve_small1(N,K,U,Ps):
    u = U
#    print u, Ps
    
    while u > 0.0:
        same_p = 1
        for i in range(N-1):
            if Ps[i] == Ps[i+1]:
                same_p += 1
            else:
                break
        
        if same_p == N:
            dp = u/N
            u = 0.0
        else:
            du = min(u, (Ps[same_p] - Ps[same_p-1])*same_p)
            u -= du
            dp = du/same_p
        
        for i in range(same_p):
            Ps[i] += dp
#        print u, Ps, dp, same_p
    
    prod = 1.0
    for p in Ps:
        prod *= p
    
    return prod
    
def solve_large(N, K, U, Ps):
    pass

T = int(raw_input())

for test_case in range(1, T+1):
    N, K = [int(s) for s in raw_input().split(" ")]
    U = float(raw_input())
    Ps = [float(s) for s in raw_input().split(" ")]
#    print B, M
    solution = solve_small1(N, K, U, sorted(Ps))
    print "Case #{}: {}".format(test_case, solution)
