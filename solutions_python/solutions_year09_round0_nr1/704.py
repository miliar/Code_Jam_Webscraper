#!/usr/bin/python

"""
Alien Language problem solution
(GCJ 2009, Qualification Round)
Author: madrezaan
"""

import sys
import re

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: alien_language.py <input file>"
    sys.exit(0)

# get constants
L, D, N = map(int, in_file.readline().split(" "))

# get dictionary
dictionary = [in_file.readline().strip() for i in range(D)]

# begin prosessing cases
for cur_case in range(N):

    # get word pattern
    s = in_file.readline().strip()
    # parse pattern
    def tolist ((a, b)):
        if a:
            return list(a[1:-1])
        else:
            return [b,]
    pattern = map(tolist, re.findall(r"(\([a-z]+\))|([a-z])", s))

    # initialize matched words list
    matched = dictionary[:]

    # filter matched words
    for i in range(L):
        matched = filter(lambda m: any(map(lambda p: p == m[i],pattern[i])), matched)

    # output result
    print "Case #%d: %d" % (cur_case + 1, len(matched))

# close input file
in_file.close()

    
        
