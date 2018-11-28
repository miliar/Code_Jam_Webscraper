#!/usr/bin/env python


if __name__ == '__main__':
    times = int(raw_input())
    for i in xrange(times):
        n, k = raw_input().split(' ')
        n = int(n)
        k = int(k)
        if (k % (2 ** n)) == ((2 ** n) - 1):
            result = "ON"
        else:
            result = "OFF"
        print "Case #%d: %s" % (i+1, result)
