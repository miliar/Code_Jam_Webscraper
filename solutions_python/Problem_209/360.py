#! /bin/python

from sys import stdin
from math import pi

T = int(stdin.readline())

for t in range(T):

    [N, K] = [int(x) for x in stdin.readline().split()]
    pancakes = []
    for _ in range(N):
        [R, H] = [int(x) for x in stdin.readline().split()]
        pancakes.append((R, H))

    side = sorted([(h * 2 * pi * r, r, h) for (r,h) in pancakes], reverse=True)
    if K > 1:
        maxRad = max([r for (_, r, _) in side[:K-1]])
    else:
        maxRad = 0

    last = max([(s + pi * max(r**2, maxRad**2)) for (s, r, h) in side[K-1:]])

    S1 = last + sum(x[0] for x in side[:K-1])

    print("Case #{}: {}".format(t+1, S1))
