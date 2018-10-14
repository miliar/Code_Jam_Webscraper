#!/usr/bin/env python

import sys

cases = []

class Case:
    def __init__(self, line):
        l = line.split()
        self.a = int(l[0])
        self.b = int(l[1])

def calc(cases):
    for c in cases:
        out = []
        count = 0
        sa = str(c.a)
        if len(sa) <= 1:
            c.out = 0
            continue
        for x in xrange(c.a, c.b):
            ans = []
            sx = str(x)
            for i in range(len(sx)-1):
                i += 1
                b = int(sx[i:] + sx[:i])
                if b >= c.a and x < b and b <= c.b and (x,b) not in ans:
                    #print x, b
                    ans.append((x,b))
                    count += 1
        c.out = count
        print count

def inputs():
    if len(sys.argv) < 2:
        print "missing input file"
        sys.exit()
    f = open(sys.argv[1], 'r')
    lines = f.readline()

    for i in xrange(int(lines)):
        line = f.readline()
        cases.append(Case(line))

def out(cases):
    for i in xrange(len(cases)):
        print "Case #%d: %s" % (i+1, cases[i].out)

def main():
   inputs()
   calc(cases)
   out(cases)

if __name__ == '__main__':
    main()

