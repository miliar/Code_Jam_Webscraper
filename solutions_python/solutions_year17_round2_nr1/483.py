#!/usr/bin/env python
import sys


def problem(fi):
    d, n = fi.readline().strip().split(' ')
    horses = []
    for i in xrange(int(n)):
        k, s = fi.readline().strip().split(' ')
        horses.append((int(k), int(s)))
    return int(d), int(n), horses


def solve(params, i):
    d, n, horses = params

    times = (float(d - k) / s for k, s in horses)
    max_time = max(times)
    return '{:.6f}'.format(d / max_time)


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
