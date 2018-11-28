#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])

    ncases = int(f.readline())
    for icase in range(ncases) :
        line = [int(i) for i in f.readline().split()]

        A, B = line[0], line[1]

        ndig = len(str(A))
        
        solution = 0

        for i in xrange(A, B+1) :
            recy = []
            for idig in range(1,ndig) :
                p = i / 10**idig + (i % 10**idig) * 10**(ndig-idig)
                if (p > i) and (p >= A) and (p <= B) and not (p in recy) :
                    solution += 1
                    recy.append(p)
                        
        print 'Case #%i:'%(icase+1),
        print solution
            
    f.close()
    
main()
