#!/usr/bin/env python
import sys
from itertools import islice
import psyco; psyco.full()

def read_input(filename):
    f = open(filename)
    testcases = int(f.readline())
    for i in xrange(testcases):
        snappers, snaps = [int(i) for i in f.readline().strip().split()]
        yield snappers, snaps

def solve(snappers, snaps):
    pwr = [True] + [False]*(snappers-1)
    switch = [False]*snappers
    for s in xrange(snaps):
        # Toggle switches
        for i in xrange(snappers):
            # 
            to_break = not pwr[i] or not switch[i]
            if pwr[i]:
                switch[i] = not switch[i]
            if to_break:
                break
        # Now see who still has power
        for i in xrange(1, snappers):
            pwr[i] = pwr[i-1] and switch[i-1]
            if not pwr[i] or not switch[i]:
                pwr[i+1:] = [False]*(snappers-(i+1))
                break

    return ('OFF', 'ON')[pwr[-1] and switch[-1]]

def main(infile):
    output = (solve(snappers, snaps) for snappers, snaps in read_input(infile))
    print "\n".join("Case #{0}: {1}".format(i+1, answer) for i, answer in enumerate(output))

if __name__ == '__main__':
    main(sys.argv[1])

