#!/usr/bin/env python

import sys


def print_result(result, i):
    sys.stdout.write("Case #%s: %s\n" % (i, result))


def readline():
    return sys.stdin.readline().rstrip('\n')


def splitline(f):
    return map(f, readline().split())


def solve():
    D, N = splitline(int)
    t = 0
    for _ in xrange(N):
        K, S = splitline(int)
        rem = D - K
        ti = float(rem) / S
        t = max(t, ti)

    s = float(D) / t
    return "%.30f" % s


def main():
    for i in range(int(readline())):
        print_result(solve(), i + 1)


if __name__ == '__main__':
    main()
