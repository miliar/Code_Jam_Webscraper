import sys
import math

def solve(N, K):
    K -= 1
    #print("N=", N, "K=", K)
    lower = 0
    upper = 1
    while upper <= K:
        #print("upper=", upper)
        #print("lower=", lower)
        lower <<= 1
        lower += 1
        upper <<= 1
        upper += 1
    #print("upper=", upper)
    #print("lower=", lower)
    mass = N - lower #how much mass left before reaching the last level of the tree
    max_level = lower+1 #at maximum this many nodes could be on this level of the tree
    P = mass / max_level #how many elements per cluster from this level
    L = mass % max_level
    X = P + ((K-lower) < L) - 1
    a = math.ceil(1.0*X/2)
    b = math.floor(1.0*X/2)
    #print("mass=", mass, "max_level=", max_level, "P=", P, "L=", L, "X=", X, "a=", a, "b=", b)
    
    return " ".join(map(str, map(int, [max(a, b), min(a, b)])))

T=int(sys.stdin.readline())
for t in range(1, T+1):
    N, K=map(int, sys.stdin.readline().split())
    res = solve(N, K)
    print "Case #"+str(t)+": "+res
