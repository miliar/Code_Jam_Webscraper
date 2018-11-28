#!/bin/env python2

tests = input()

for test in range(tests):
    line = raw_input().split(' ')
    X, R, C = int(line[0]), int(line[1]), int(line[2])
    if X >= 7:
        # Richard can always choose an X-omino with a 1x1 hole, which
        # is then unfillable
        print "Case #{0}: RICHARD".format(test+1)
        continue
    if (R * C) % X != 0:
        # the area of the region cannot possibly be filled
        # by an integer number of X-ominos. Richard will always
        # win, regardless of selection.
        print "Case #{0}: RICHARD".format(test+1)
        continue
    if X <= 2:
        # in the case of X = 1, trivially solvable by Gabriel regardless 
        # of board shape, and in X = 2, all boards with non-odd area can
        # be solved (and odd areas are screened in previous if)
        print "Case #{0}: GABRIEL".format(test+1)
        continue

    # board rotations are identical, so normalize board to be 
    # short and wide
    if C < R:
        R, C = C, R

    # bruteforced on paper; all other solvable variations with X={3,4} and R,C in [1,4]
    solvable = [
        (4,4,4),
        (4,3,4),
        (3,3,4),
        (3,3,3),
        (3,2,3),
    ]

    print "Case #{0}: {1}".format(test+1, "GABRIEL" if (X,R,C) in solvable else "RICHARD")
