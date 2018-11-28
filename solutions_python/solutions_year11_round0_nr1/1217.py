#!/usr/bin/env python

from collections import defaultdict

f = open('cases.txt', 'r')

def other(bot):
    return 'B' if bot is 'O' else 'O'

def pairs(iter):
    return zip(iter[::2], iter[1::2])

cases = int(f.readline())

for i in range(cases):
    case = f.readline().split()[1:]
    pos = defaultdict(lambda: 1)
    ahead = defaultdict(int)
    total = 0
    for (bot, target) in pairs(case):
        target = int(target)
        distance = abs(pos[bot] - target)
        steps = max(distance - ahead[bot], 0) + 1
        ahead[other(bot)] += steps
        total += steps
        ahead[bot] = 0
        pos[bot] = target
    print "Case #%d: %d" % (i + 1, total)
