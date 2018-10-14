# -*- coding: utf-8 -*-
from sys import stdin

def main():
    line = stdin.readline().strip()
    s = "welcome to code jam"
    x = [1] + [0]*(len(s))
    for c in line:
        for i, d in enumerate(s):
            if c == d:
                x[i+1] = (x[i+1] + x[i])%10000
    return str(x[len(s)]).rjust(4, '0')

tno = int(stdin.readline())
for i in xrange(0, tno):
    print "Case #%d: %s"%(i+1, main())