#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    S, K = input().split()
    S = [ 1 if s=='+' else -1 for s in S]
    K = int(K)
    
    pcnt = 0
    n = 0
    for i in range(len(S)-K+1):
        if S[i] == -1:
            for j in range(K):
                S[i+j] *= -1
            n += 1
    for s in S[-K+1:]:
        if s == -1:
            n = 'IMPOSSIBLE'
            break
    print("Case #{0}: {1}".format(t, n))
