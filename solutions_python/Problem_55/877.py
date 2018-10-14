#!/usr/bin/env python

# CodeJam 2010 - Problem C: Theme park
# David Adam <zanchey@ucc.gu.uwa.edu.au>

import sys

if __name__ == "__main__":
    inputfile = open(sys.argv[1])
    outputfile = open(sys.argv[1] + '.out', 'w')
    
    cases = long(inputfile.readline())
    
    for casen in xrange(1, cases + 1):
        profit = long(0)
        runs, size, groupn = (long(x) for x in inputfile.readline().split())
        groups = [long(x) for x in inputfile.readline().split()]
        
        for run in xrange(runs):
            print "Case %d, run %d" % (casen, run)
            space = size
            coaster = []
            while True:
                # try and get the next group
                try:
                    nextgroup = groups.pop(0)
                except IndexError:
                    # perfect - no more groups
                    # unload the rollercoaster
                    groups.extend(coaster)
                    break
                
                # does it fit on the coaster?
                if nextgroup <= space:
                    # put it on
                    coaster.append(nextgroup)
                    profit += nextgroup
                    space = space - nextgroup
                else:
                    # put it back on the list
                    groups.insert(0, nextgroup)
                    # unload the rollercoaster
                    groups.extend(coaster)
                    # and break out.
                    break
        
        outputfile.write("Case #%d: %d\n" % (casen, profit))