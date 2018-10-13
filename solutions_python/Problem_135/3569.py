#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

r_lin = lambda: sys.stdin.readline()
r_int = lambda: int(sys.stdin.readline())

num_cases = r_int()

for case in xrange(num_cases):
    chosen_row = r_int()
    
    for row in xrange(4):
        if row + 1 == chosen_row:
            first_row_elements = [int(x) for x in r_lin().strip().split()]
        else:
            r_lin()

    chosen_row = r_int()
    
    for row in xrange(4):
        if row + 1 == chosen_row:
            second_row_elements = [int(x) for x in r_lin().strip().split()]
        else:
            r_lin()

    possible_elements = set(first_row_elements) & set(second_row_elements)

    if len(possible_elements) == 1:
        print "Case #{}: {}".format(case + 1, list(possible_elements)[0])
    elif len(possible_elements) == 0:
        print "Case #{}: Volunteer cheated!".format(case + 1)
    else:
        print "Case #{}: Bad magician!".format(case + 1)
        

