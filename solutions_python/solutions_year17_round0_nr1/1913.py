#!/usr/bin/env python3

def flip(ps, x, k):
    nps = list(ps)
    for i in range(x, x + k):
        nps[i] = '-' if nps[i] == '+' else '+'
    return ''.join(nps)

def flips(ps, k):
    n = len(ps)
    return [flip(ps, x, k) for x in range(n - k + 1)]

T = int(input())

for t in range(1, T+1):
    ps, k = input().split()
    k = int(k)
    n = len(ps)

    vis = {ps}

    last = {ps}


    i = 0
    TARGET = '+' * n

    while TARGET not in vis:
        new = set()
        for p in last:
            for flipped in [f for f in flips(p, k) if f not in vis]:
                new.add(flipped)
                vis.add(flipped)
        if len(new) == 0:
            i = None
            break
        last = new
        i += 1

    print("Case #{}: {}".format(t, "IMPOSSIBLE" if i is None else i))
