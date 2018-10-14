#!/usr/bin/env python
import sys


def bad_pos(s):
    for i in xrange(len(s) - 1):
        if s[i] > s[i + 1]:
            return i
    return -1


def solve(s):
    if len(s) < 2:
        return s
    i = bad_pos(s)
    if i < 0:
        return s
    s_new = s[:i] + str(int(s[i]) - 1)
    return solve(s_new) + '9' * len(s[i+1:])


if __name__ == '__main__':
    sys.stdin.readline()
    for num, line in enumerate(sys.stdin, 1):
        x = line.strip()
        y = int(solve(x))
        print "Case #{0}: {1}".format(num, y)
