#!/usr/bin/env python

import sys

cases = []

class Case:
    def __init__(self, line):
        l = line.split()
        self.N = int(l[0])
        self.S = int(l[1])
        self.p = int(l[2])
        self.totals = [int(x) for x in l[3:]]

def calc(cases):
    for c in cases:
        sure = 0
        poss = 0
        for t in c.totals:
            avg = t/3
            extra = t%3
            max = avg+extra
            if avg and extra == 0:
                max += 1

            if avg >= c.p:
                sure += 1
            elif max >= c.p:
                if avg == c.p-1:
                    if extra:
                        sure += 1
                    else:
                        poss += 1
                elif avg == c.p-2:
                    if extra == 2:
                        poss += 1
                else:
                    import pdb; pdb.set_trace()

            '''elif avg == c.p-1:
                if extra >= 1:
                    sure += 1
                else:
                    poss += 1
            elif avg == c.p - 2:
                if extra == 2:
                    poss += 1'''

        c.out = sure + min(poss, int(c.S))

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

