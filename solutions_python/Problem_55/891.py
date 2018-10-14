#!/usr/bin/python
# count.py
# michael.tartar@gmail.com
#
# Usage : count.py data_file_name

import sys
import pdb

DEBUG = 0

if len(sys.argv) != 2:
    print "USAGE: ./%s data_file_name"%sys.argv[0]
    sys.exit(1)

filename = sys.argv[1]
f = open(filename, "r")

# Number of test cases
numberTestCases = int( f.readline().strip('\n') )

# Test cases
for itest in range(numberTestCases):

    # Integers
    integers = f.readline().strip('\n')
    integers = integers.split(" ")
    R = int(integers[0])
    k = int(integers[1])
    N = int(integers[2])
  
    # Sizes
    gi = f.readline().strip('\n')
    gi = gi.split(" ")
    sizes = [ int(s) for s in gi ]

    # -------
    # Solver
    # -------

    count = 0

    # Loop (roller coast runs)
    for irun in range(R):

        # Seats available
        seats = k
        ngroup = 0

        # Get groups in the roller coaster
        while sizes[0] <= seats and ngroup < N:
            size = sizes.pop(0)
            sizes.append(size)
            ngroup += 1 
            seats -= size
            count += size

    # Output
    print "Case #%i: %i"%(itest+1, count)
