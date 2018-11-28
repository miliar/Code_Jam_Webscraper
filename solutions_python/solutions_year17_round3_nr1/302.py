
from collections import defaultdict

from math import pi

def do():
    N,K = map(int, input().split())

    R,H = zip(*sorted([[int(x) for x in input().split()] for _ in range(N)], reverse=True))

    x = sorted(((R[i],2*R[i]*H[i]*pi,H[i]) for i in range(N)), reverse=True)

    # If one pancake, pick the best one
    if K == 1:
        print('%.10f' % max(2*R[i]*H[i]*pi + R[i]**2*pi for i in range(N)))
        return

    # Pick best
    best = -1
    for i in range(N):
        # Assume we pick a pancake with largest radius
        res = x[i][1] + x[i][0]**2*pi
        y = sorted(x[i+1:], reverse=True, key=lambda e: e[1])[:K-1] # Pick best k-1 other
        if len(y) == K-1: # Picked right number?
            res2 = sum(e[1] for e in y) 
            best = max(best, res+res2)
    print('%.10f' % best)
    
    #x = x[:K]
    #res = sum(e[0] for e in x)*pi + max(e[1] for e in x)**2*pi
    #print('%.10f' % (res))
    
    #M = [[0]*N for _ in range(K+1)] # M[k][n]
    #for i in range(N):
    #    M[1][i] = 2*pi*R[i]*H[i] + pi*(R[i]**2)
    #for k in range(2,K+1):
    #    for i in range(N):
    #        best = -1
    #        for j in range(i+1,N):
    #            best = max(best, 2*pi*R[j]*H[j] + pi*(R[i]**2-R[j]**2) +
    #                       M[k-1][j])
    #            print(2*pi*R[j]*H[j] + pi*(R[i]**2-R[j]**2), '+', M[k-1][j])
    #            print('::',k,',',i,j,best)
    #        
    #        M[k][i] = best
    #for r in M:
    #    print(r)
    #print('-----')
    #maxi = max(M[K])
    #print(maxi)        
    

t = int(input())

import sys

for _ in range(t):
    print(_,file=sys.stderr)
    print('Case #%d: '%(_+1), end='')
    do()
