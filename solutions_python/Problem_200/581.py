#!/usr/bin/env python
import sys


def problem(fi):
    r1 = fi.readline().strip()
    return int(r1)


def solve(params, i):
    n = params

    sn = list(str(n))

    min_digit = int(sn[-1])
    for i in xrange(len(sn) - 1, -1, -1):
        digit = int(sn[i])
        if digit > min_digit:
            for j in xrange(i + 1, len(sn)):
                sn[j] = '9'
            sn[i] = str(digit - 1)
            min_digit = digit - 1
        else:
            min_digit = min(min_digit, digit)

    return int(''.join(sn))


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), i)
            fo.write('Case #{0}: {1}\n'.format(i + 1, res))
            fo.flush()
