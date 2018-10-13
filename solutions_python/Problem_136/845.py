#! /usr/bin/python
import sys


def caculate(c, f, x):

    def formula(y, n):
        if not n:
            return y / 2
        return y / (2 + n * f) + xoffset

    nn = 0
    minX = 9999
    while True:
        xoffset = sum([c / (2 + i * f) for i in range(nn)])
        curX = formula(x, nn)
        if curX < minX:
            minX = curX
        else:
            return minX
        nn += 1

fh = open(sys.argv[1])

count = int(fh.readline())

for i in range(count):
    (c, f, x) = fh.readline().split()
    print "Case #%d:" % (i + 1),
    print caculate(float(c), float(f), float(x))
