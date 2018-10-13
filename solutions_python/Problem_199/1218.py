from sys import *
import math

def readints():
    return list(map(int, stdin.readline().split()))

def solve(S, K):
    # print(S)

    k = 0
    while k < len(S) and S[k] == "+":
        k += 1

    S = S[k:]

    if len(S) == 0:
        return 0
    if len(S) < K:
        return float('-inf')
    else:
        S = list(S)
        for k in range(K):
            S[k] = "+" if S[k] == "-" else "-"
        S = ''.join(S)
        return solve(S, K) + 1

T, = readints()

for i in range(T):
    S, K = stdin.readline().split()
    K = int(K)

    res = 0
    while len(S):
        k = 0
        while k < len(S) and S[k] == "+":
            k += 1

        S = S[k:]

        if len(S) == 0:
            break
        if len(S) < K:
            res =  float('-inf')
            break
        else:
            S = list(S)
            for k in range(K):
                S[k] = "+" if S[k] == "-" else "-"
            S = ''.join(S)
            res += 1

    if res < 0:
        res = "IMPOSSIBLE"

    print("Case #{}: {}".format(i + 1, res))
