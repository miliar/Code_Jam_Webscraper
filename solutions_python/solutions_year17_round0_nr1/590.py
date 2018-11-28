#! /bin/python

from sys import stdin

def flip(i, S, K):
    for k in range(i, i+K):
        if S[k] == '+':
            S[k] = '-'
        else:
            S[k] = '+'

T = int(stdin.readline().strip())

for t in range(T):
    (S, K) = stdin.readline().split()
    K = int(K)
    S = [c for c in S]

    if K > len(S):
        print("Case #{}: IMPOSSIBLE".format(t+1))
        continue

    c = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            flip(i, S, K)
            c += 1
    for i in range(len(S)-K, len(S)):
        if S[i] == '-':
            c = -1;

    if c == -1:
        print("Case #{}: IMPOSSIBLE".format(t+1))
    else:
        print("Case #{}: {}".format(t+1, c))
