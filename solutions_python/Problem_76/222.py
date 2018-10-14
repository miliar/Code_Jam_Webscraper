#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        ncandy = int(f.readline().strip())
        candy = [int(s) for s in f.readline().split()]

        candy.sort()
        
        solution = 0
        for k in range(1,ncandy) :
            sum_left  = reduce(lambda x, y: x ^ y, candy[:k])
            sum_right = reduce(lambda x, y: x ^ y, candy[k:])

            if sum_left == sum_right :
                solution = sum(candy[k:])
                break

        print 'Case #%i:'%(icase+1),
        if solution == 0 :
            print "NO"
        else:
            print solution 
    
    f.close()

main()
