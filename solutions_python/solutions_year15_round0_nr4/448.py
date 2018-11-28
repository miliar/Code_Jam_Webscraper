#!/usr/bin/python
__author__ = 'sbuono'

import sys

f = open(sys.argv[1])

nbTestCases = f.readline().strip()

case = 1
for line in f.readlines() :

    winner = "GABRIEL"

    line = line.strip()

    ll = line.split()

    X = int(ll[0])
    R = int(ll[1])
    C = int(ll[2])

    # general rules
    if X > 6 :
        winner = "RICHARD"
    if (R * C) % X != 0 :
        winner = "RICHARD"
    if C < X and R < X :
        winner = "RICHARD"
    tmp = ((X / 2) + (X % 2))
    if C < tmp or R < tmp:
        winner = "RICHARD"
    if X > 3 and (R * C) <= ( X * 2 ) :
        winner = "RICHARD"

    print "Case #%d: %s" % (case, winner)


    case += 1