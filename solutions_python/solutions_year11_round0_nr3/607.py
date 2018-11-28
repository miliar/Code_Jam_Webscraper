#! /usr/bin/env python
#coding=utf-8

import sys
def main():
    if len(sys.argv) < 2:
        return
    xor = lambda x, y : x ^ y
    f = open(sys.argv[1], "r").read().splitlines()
    t = int(f[0])
    for i in xrange(1, t + 1):
        n = int(f[2 * i - 1])
        s = [int(o) for o in f[2 * i].split()][:n]
        if reduce(xor, s) == 0:
            min = reduce(lambda x, y:x if x < y else y, s)
            print "Case #%d: %d" % (i, sum(s) - min)
        else:
            print "Case #%d: NO" % i

if __name__ == '__main__':
    main()
