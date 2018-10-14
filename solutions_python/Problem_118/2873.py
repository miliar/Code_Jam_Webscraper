#!/usr/bin/env python

import sys
import math

infile = open(sys.argv[1], 'rb')

lines = infile.readlines()

n_cases = int(lines.pop(0))

def is_palindrome(x):
    str_x = str(int(x))
    n = len(str_x)
    for ichar in range(n/2):
        if str_x[ichar] != str_x[n-1-ichar]:
            return False
    return True

for icase in range(1, n_cases+1):
    # read case
    bounds = [int(x) for x in lines.pop(0).split()]
       
    # check each
    n_fns = 0
    for x in range(bounds[0], bounds[1]+1):
        sqrt = math.sqrt(x)
        if sqrt - math.floor(sqrt) == 0:
            if is_palindrome(x):
                if is_palindrome(sqrt):
                    n_fns += 1

    print "Case #%d: %s" % (icase,n_fns)

    # discard blank row
 #   if len(lines) > 0:
 #       discard = lines.pop(0)
