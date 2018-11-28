#!/usr/bin/env python2

import os, sys


def solve ( row1, row2 ):
    res = row1.intersection( row2 )

    if len( res ) == 1:
        return str( res.pop() )

    if len( res ) == 0:
        return "Volunteer cheated!"

    return "Bad magician!"


fd = sys.stdin

line = fd.readline()
sets = int( line )+1

for case in range(1, sets):
    ans1 = int( fd.readline() )
    row1 = None
    for row in range( 4 ):
        line = fd.readline()
        if row == ans1 - 1:
            row1 = set( [ int( x ) for x in line.split() ] )

    ans2 = int( fd.readline() )
    row2 = None
    for row in range( 4 ):
        line = fd.readline()
        if row == ans2 - 1:
            row2 = set( [ int( x ) for x in line.split() ] )

    nline = solve( row1, row2 )
    print "Case #%s: %s" % (case, nline)

fd.close()
