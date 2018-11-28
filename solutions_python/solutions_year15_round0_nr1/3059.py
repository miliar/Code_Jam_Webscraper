#!/usr/env/python

from sys import stdin

def solve_prob():
    raw = stdin.readline().strip().split()
    people = raw[1]
    added = 0
    clapping = 0
    for i in range(0, int(raw[0]) + 1):
        cur = int(people[i])
        if cur == 0:
            continue
        if clapping < i:
            invited = i - clapping
            added += invited
            clapping += invited
        clapping += cur
    return str(added)

nb = int(stdin.readline().strip())
for i in range(1, nb + 1):
    print('Case #{}: {}'.format(i, solve_prob()))
