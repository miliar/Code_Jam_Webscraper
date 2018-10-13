#!/usr/bin/env python
import sys


def problem(fi):
    r1 = fi.readline().strip()
    s, k = r1.split(' ')
    return list(s), int(k)


def solve(params, i):
    s, k = params

    count = 0
    for i in xrange(len(s) - k + 1):
        if s[i] == '+':
            continue
        if s[i] == '-':
            count += 1
            for j in xrange(i, i + k):
                s[j] = '-' if s[j] == '+' else '+'

    if '-' not in s:
        return count

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
