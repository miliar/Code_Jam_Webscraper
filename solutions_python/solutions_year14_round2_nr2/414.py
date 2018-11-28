#!/usr/bin/env python
"""gcj code. """

from sys import stdin


def main():
    x = stdin.readline()
    y = int(x)
    for i in xrange(1, y + 1):
        print "Case #%d: %s" % (i, realmain(i))


def realmain(case):
    l = stdin.readline()
    l = l.split()
    a = int(l[0])
    b = int(l[1])
    k = int(l[2])
    res = 0
    for x in xrange(0,a):
        for y in xrange(0,b):
            if (x & y) < k:
                res = res + 1
    return "%d" % res


#####################################################

if __name__ == '__main__':
    main()
