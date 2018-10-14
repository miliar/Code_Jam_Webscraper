#!/usr/bin/python

from sys import stdin, stdout

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a

C = stdin.readline()
results = []
case_num = 1
for line in stdin.readlines():
    events = [int(n) for n in line.split(' ')]
    size = events.pop(0)
    events.sort()

    diffs = [events[i] - events[i-1] for i in range(1, size)]
    gap = diffs[0]
    for n in diffs[1:]:
        gap = gcd(gap, n)

    next = - events[0] % gap
    results.append("Case #%d: %s\n" % (case_num, next))
    case_num += 1

stdout.writelines(results)
