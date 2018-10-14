#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for i in range(ncases) :
        n = int(f.readline().strip())

        nums = [int(s) for s in f.readline().split()]

        print len(nums)
        
        cycles = []
        used = []

        while len(used) < n:

            cycles.append([])
            for k in xrange(1,n+1) :
                if k not in used :
                    p = k
                    break

            while p not in cycles[-1] :
                cycles[-1].append(p)
                p = nums[p-1]
            used = used + cycles[-1]

        #print cycles

        hits = 0
        for c in cycles :
            if len(c) > 1 :
                hits = hits + len(c)

        print 'Case #%i:'%(i+1), 
        print '%-.6f' % hits
    
    f.close()

main()
