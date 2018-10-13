import sys
from itertools import combinations


def is_recycled_pair(n, m):
    ns, ms = map(str, [n, m])
    i = 0
    found = False
    while 1:
        f = ms.find(ns[0], i)
        if f == -1:
            break
        if ms[f:] + ms[:f] == ns:
            found = True
            break
        i = f + 1
    return found


def find(a, b):
    groups = {}
    for i in range(a, b + 1):
        s = tuple(sorted(str(i)))
        try:
            groups[s].append(i)
        except KeyError:
            groups[s] = [i]

    groups = [g for g in groups.values() if len(g) > 1]

    s = 0
    for g in groups:
        for pair in combinations(g, 2):
            n, m = sorted(pair)
            if is_recycled_pair(n, m):
                s += 1
    return s

cases = int(sys.stdin.readline())
for i in range(cases):
    a, b = map(int, sys.stdin.readline().strip().split())
    print 'Case #%d: %d' % (i + 1, find(a, b))


