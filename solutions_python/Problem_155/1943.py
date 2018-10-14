#!/usr/bin/env python 3
for T in range(int(input())):
    Sm, S = input().split()
    Sm = int(Sm)
    S = list(map(int, list(S)))
    tot = 0
    f = 0
    for i in range(Sm + 1):
        if tot < i:
            f += i - tot
            tot += i - tot
        tot += S[i]
    print("Case #{0}: {1}".format(T+1, f))
