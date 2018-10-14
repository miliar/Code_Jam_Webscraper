from sys import stdin, setrecursionlimit
from math import inf

setrecursionlimit(2500)

def flip(lst):
    return [(x + 1) % 2 for x in lst]

def solve(lst, k, flips):
    if len(lst) < k:
        return flips if 0 not in lst else "IMPOSSIBLE"

    if lst[0] == 0:
        lst[:k] = flip(lst[:k])
        return solve(lst[1:], k, flips+1)
    else:
        return solve(lst[1:], k, flips)

T = int(next(stdin))

for t in range(1, T+1):
    S, K = next(stdin).strip().split(" ")
    S = [0 if s == "-" else 1 for s in S]
    K = int(K)

    print("Case #{0}: {1}".format(t, solve(S, K, 0)))
