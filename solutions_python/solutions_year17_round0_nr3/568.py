#!/usr/bin/env python
import heapq
import sys


def problem(fi):
    r1 = fi.readline().strip()
    n, k = r1.split(' ')
    return int(n), int(k)


def solve(params, i):
    print i
    n, k = params
    q = [-n]

    count = {n: 1}

    maxs, mins = None, None
    i = 0
    while i < k:
        size = -q[0]

        c = count[size]
        del count[size]
        heapq.heappop(q)

        maxs = size // 2
        mins = size - maxs - 1

        if maxs:
            if maxs not in count:
                heapq.heappush(q, -maxs)
                count[maxs] = c
            else:
                count[maxs] += c
            if mins:
                if mins not in count:
                    heapq.heappush(q, -mins)
                    count[mins] = c
                else:
                    count[mins] += c

        i += c

    return '{} {}'.format(maxs, mins)


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
