#!/usr/bin/python
import sys

# Cookie Clicker

def seconds(nf, c, f, x):
    t = 0.0
    for i in xrange(nf):
        t += c / (2.0 + i*f)
    t += x / (2.0 + nf*f)
    return t

def mintime(c, f, x):
    nf = 0
    t = seconds(nf, c, f, x)
    while True:
        next = seconds(nf+1, c, f, x)
        if next < t:
            t = next
            nf += 1
        else:
            break
    return t

lines = [l.rstrip() for l in sys.stdin.readlines()]
for i in xrange(int(lines.pop(0))):
    nf, r = 0, 2.0
    c, f, x = [float(l) for l in lines[i].split()]
    result = "{0:.7f}".format(mintime(c, f, x))
    print "Case #%u: %s" % (i + 1, result)
