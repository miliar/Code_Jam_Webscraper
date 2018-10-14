#! /bin/python

from sys import stdin
from math import inf

T = int(stdin.readline())

for t in range(T):
    [D, N] = [int(x) for x in stdin.readline().split()]
    horses = []
    for _ in range(N):
        [K, S] = [int(x) for x in stdin.readline().split()]
        horses.append((K, S))

    time = max([(D-k)/s for (k, s) in horses])
    maxspeed = D / time
    print("Case #{}: {}".format(t+1, maxspeed))
