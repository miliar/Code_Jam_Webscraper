#!/usr/bin/python

import sys

f = sys.stdin


T = int(f.readline())

for index in range(1, T+1):
    [N, X] = map(int, f.readline().split())
    S = map(int, f.readline().split())
    S.sort()
    
    if len(S) != N:
        print("Error")
        exit()
    
    l = 0
    r = N-1
    
    count = 0
    
    while l <= r:
        if l == r:
            count += 1
            l += 1
        elif S[l] + S[r] <= X:
            count += 1
            l += 1
            r -= 1
        else:
            count += 1
            r -= 1
            
    print("Case #{}: {}".format(index, count))