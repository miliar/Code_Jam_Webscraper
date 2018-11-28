#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys

def main(argv):
    f = open(argv[0], "rb")
    num = int(f.readline())
    
    for n in xrange(1,num+1):
        l = f.readline().split()
        snappers = int( l[0] )
        snaps = int( l[1] )
        if (snaps + 1) % (2 ** snappers) == 0:
            print "Case #%d: ON" % n
        else:
            print "Case #%d: OFF" % n     


if __name__ == "__main__":
    main(sys.argv[1:])

