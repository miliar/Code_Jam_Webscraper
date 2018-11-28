#!/usr/bin/python

from sys import argv
import fileinput

def recycle(n):
    r = []
    d = 10
    digits = len(str(n))
    for i in xrange(digits-1):
        m = int(str(n%d) + str(n/d))
        if len(str(m)) == digits:
            r.append(m)
        d *= 10
    return r

def find(a, b):
    u = {}
    for n in xrange(a, b+1):
        for m in recycle(n):
            if n < m <= b:
                u[str(n)+str(m)] = True
    return len(u)

i = 1
for line in fileinput.input():
    if fileinput.isfirstline():
        continue

    print "Case #" + str(i) + ":",
    i += 1
    (a, b) = line.split()
    print find(int(a), int(b))	
