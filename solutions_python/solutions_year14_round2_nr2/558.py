#!/usr/bin/env python
import sys


def problem(j, fi):
    a, b, k = [int(i) for i in fi.readline().strip().split(' ')]
    return a, b, k

def solve(params, problem_id):
    a, b, k = params

    cnt = 0

    for i in xrange(a):
        for j in xrange(b):
            cnt += (i & j < k)
    return cnt


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(1, total + 1):
            print "Processing case #{0}".format(i)
            res = solve(problem(i, fi), i)
            fo.write('Case #{0}: {1}\n'.format(i, res))
            fo.flush()
