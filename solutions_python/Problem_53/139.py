#!/usr/bin/env python

def snap2(N, K):
    return not ((K + 1) % 2 ** N)


if __name__ == '__main__':
    import sys

    f = open(sys.argv[1], 'r')
    i = 0
    f.readline()
    for line in f:
        i += 1
        line = line.strip().split()
        N = int(line[0])
        K = int(line[1])
        res = "ON" if snap2(N, K) else "OFF"
        print "Case #%s: %s" % (i, res)

