#!/usr/bin/python3


T = int(input())


for t in range(T):
    
    D, N = [int(x) for x in input().split()]
    
    KS = []
    for i in range(N):
        KS.append(tuple([int(x) for x in input().split()]))
        
    
    maxT = 0
    for K, S in KS:
        T = (D - K)/S
        
        if T > maxT:
            maxT = T
    
    print("Case #{0}: {1}".format(t+1, D/maxT))


