#!/usr/bin/python

import sys

lines = int(sys.stdin.readline())

def solve(bits, n, k):
    solved = (((1 << (n - 1)) - 1) << 1) | 1
    flipper = (((1 << (k - 1)) - 1) << 1) | 1
    if bits == solved: return 0
    queue = [bits]
    dists = { bits : 0 }

    while len(queue) > 0:
        cur = queue[0]
        queue = queue[1:]
        cdist = dists[cur]
        for i in range(n - k + 1):
            new = cur ^ (flipper << i)
            if not new in dists:
                if new == solved: return cdist + 1
                dists[new] = cdist + 1
                queue += [new]

    return -1


for i in range(1, lines+1):
    line = sys.stdin.readline().strip()
    s, k = tuple(line.split(' '))
    s = "".join(['1' if x == '+' else '0' for x in s])
    k = int(k)

    sol = solve(int(s, 2), len(s), k)
    print 'Case #%s: %s' % (i, sol if sol >= 0 else 'IMPOSSIBLE')
