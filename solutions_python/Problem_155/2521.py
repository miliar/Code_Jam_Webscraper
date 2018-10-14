#!/usr/bin/env python3

def solve():
    S_max, S_is = input().split()
    S_max = int(S_max)

    S = list(map(int, S_is))

    have = 0
    needed = 0

    for i in range(0, len(S)):
        if have < i:
            delta = i-have
            needed += delta
            have += delta
        have += S[i]
    return needed

    

T = int(input())

for i in range(1, T+1):
    print("Case #{}: {}".format(i, solve()))
