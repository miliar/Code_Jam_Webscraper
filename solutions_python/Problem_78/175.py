#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for i in range(ncases) :

        N, PD, PG = [int(w) for w in f.readline().split()]

        print N, PD, PG
        
        possible = True
        if PG == 100 and PD < 100 :
            possible = False
        elif PG == 0 and PD > 0 :
            possible = False
        else :
            if N < 100 :
                largest_t = 1
                for t in [100, 50, 25, 20, 10, 5, 4, 2] :
                    if PD % t == 0 :
                        largest_t = t
                        break
                if N < 100 / largest_t :
                    possible = False

        print 'Case #%i:'%(i+1), 
        if possible :
            print "Possible"
        else:
            print "Broken"
    
    f.close()

main()
