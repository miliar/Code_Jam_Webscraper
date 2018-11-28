import os, sys

data = open(sys.argv[1], "r")
lines = int(data.readline())

for i in xrange(lines):
    n, k = [int(x) for x in data.readline().split()]
    mask = (1 << n) - 1
    print "Case #%d:" % (i + 1),
    if (k & mask) == mask:
        print "ON"
    else:
        print "OFF"
