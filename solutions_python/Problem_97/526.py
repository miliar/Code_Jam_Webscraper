#!/usr/bin/python

"""
Recycled Numbers problem solution
(GCJ 2012, Qualification Round)
Author: a5kin
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: recycled_numbers.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    A, B = map(int, in_file.readline().split(" "))
    num_len = len(str(A))
    pow10 = 1
    for i in range(num_len - 1):
        pow10 *= 10
    num_pairs = 0
    # seek pairs
    for n in range(A, B + 1):
        used = []
        m = n
        for i in range(1, num_len):
            last = m % 10
            m = last * pow10 + (m - last) // 10
            if n < m and m <= B and m not in used:
                used.append(m)
                num_pairs += 1
    # output results
    print "Case #%d: %s" % (cur_case + 1, num_pairs)

# close input file
in_file.close()

    
        
