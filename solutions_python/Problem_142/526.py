#!/usr/bin/env python
"""gcj code. """

from sys import stdin


def main():
    x = stdin.readline()
    y = int(x)
    for i in xrange(1, y + 1):
        print "Case #%d: %s" % (i, realmain(i))


def realmain(case):
    x = stdin.readline()
    N = int(x)
    a = stdin.readline().rstrip()
    b = stdin.readline().rstrip()
    return fmt_answer(simple_dist(a, b))


def simple_dist(a, b):
    a = parts(a)
    b = parts(b)
    n = len(a)
    retval = 0
    if len(b) != n:
        return -1
    for i in range(0, n):
        AA = a[i]
        BB = b[i]
        if AA[0] != BB[0]:
            return -1
        else:
            retval = retval + abs(AA[1]-BB[1])
    return retval


def parts(s):
    retval = []
    prev = ''
    c = 0
    for x in s:
        if x == prev:
            c = c + 1
        else:
            retval.append([prev, c])
            prev = x
            c = 0
    retval.append([prev, c])
    return retval


def fmt_answer(n):
    if n < 0:
        return 'Fegla Won'
    return '%d' % n

#####################################################

if __name__ == '__main__':
    main()
