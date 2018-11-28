import sys


def solve(S, K):
    flip = 0
    possible = True
    for i in range(len(S)):
        if S[i] == '-' and i <= len(S) - K:
            for j in range(K):
                S[i + j] = '+' if S[i + j] == '-' else '-'
            flip += 1
        if S[i] != '+':
            possible = False
    return flip if possible else "IMPOSSIBLE"


T = int(input())
for i in range(T):
    strin = input()
    s, k = strin.split()
    S = list(s)
    K = int(k)
    print('Case #{}: {}'.format(i+1, solve(S, K)))






