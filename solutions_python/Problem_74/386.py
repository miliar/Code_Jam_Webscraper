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
        l = f.readline().strip().split()  
        nops = int(l[0])
        if len(l) != (nops * 2 + 1):
            print "Error got ", l
            sys.exit(1)

        opos = 1
        otime = 0
        bpos = 1
        btime = 0
        ctime = 0
        
        idx = 0
        for i in xrange(nops):
            idx += 1
            rob = l[idx]
            idx += 1
            topos = int(l[idx])

            if ( rob == "O" ):
                otime += abs(topos - opos) + 1
                if ( otime > ctime ):
                    ctime = otime
                    opos = topos
                else:
                    otime = ctime + 1
                    ctime = otime
                    opos = topos 
            elif ( rob == "B" ):
                btime += abs(topos - bpos) + 1
                if ( btime > ctime ):
                    ctime = btime
                    bpos = topos
                else:
                    btime = ctime + 1
                    ctime = btime
                    bpos = topos 
            else:
                print "Error rob = ", rob
                sys.exit(1)
        
        print "Case #%d: %d" % (nt + 1, ctime)
            

if __name__ == "__main__":
    main()

