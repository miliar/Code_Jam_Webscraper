#!/usr/bin/env python3

from sys import stdin


T = int(stdin.readline())

for tc in range(T):
    s_max, s = stdin.readline().strip().split()

    friends, clapping = 0, 0
    for i, s_i in enumerate(int(x) for x in s):
        new_friends = max(0, i - clapping)
        friends += new_friends
        clapping += new_friends + s_i

    print("Case #%d: %d" % (tc + 1, friends))
