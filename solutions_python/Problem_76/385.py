#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os
import math
import binascii
                            
def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for nt in xrange(ntest):
        ncandy = int(f.readline().strip())
        l = [ int(x) for x in f.readline().strip().split() ]   
        if len(l) != ncandy:
            print "Error got ", l
            sys.exit(1)
	        
        tsum = 0L
        txor = 0L
        for i in xrange(ncandy):
            tsum += l[i]
            txor ^= l[i]

        if ( txor != 0 ):
            print "Case #%d: NO" % (nt + 1)
        else:
            print "Case #%d: %d" % (nt + 1, tsum - min(l))
            

if __name__ == "__main__":
    main()

