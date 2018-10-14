#!/usr/bin/env python2

import sys

input_data = sys.stdin.readlines()

T = int(input_data[0])

for index, line in enumerate(input_data[1:]):

    X, R, C = map(int, line.strip().split())
    winner = 'GABRIEL'


    if X >= 7:
        # If x >=7, RICHARD wins since at least one omino has an unreachable-blank
        winner = 'RICHARD'
    elif (R * C) % X != 0:
        # If the number of squares to fill is not a multiple of X, it is not possible
        # to cover them all
        winner = 'RICHARD'
    elif R < X and C < X:
        # If both dimensions are less than X, then the 1xX omino cannot fit
        winner = 'RICHARD'
    elif R <= X -2 or C <= X -2 :
        # If either dimenion is less than X -2, an omino exists that either fits in no
        # orientation OR cannot be placed without leaving an unreachable blank against
        # a wall
        winner = 'RICHARD'

    print "Case #%d: %s" % (index+1, winner)


