#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os


def numinter( wset, nw ):
    ah, bh = nw
    ni = 0
    for i in wset:
        ao, bo = i
        if ao < ah and bo > bh:
            ni += 1
        elif ao > ah and bo < bh:
            ni += 1
    return ni


def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for t in xrange(ntest):
        n = int(f.readline().strip())

        ni = 0
        wireSet = []
        for w in xrange(n):
            l = [ int(x) for x in f.readline().strip().split() ]   
            if len(l) != 2:
                print "Error ", l
                sys.exit(1)
            ah = l[0]
            bh = l[1]
            ni += numinter( wireSet, (ah,bh) )
            wireSet.append((ah,bh))

        print "Case #%d: %d" % (t+1, ni)

if __name__ == "__main__":
    main()

