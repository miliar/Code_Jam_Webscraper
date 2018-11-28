#/usr/bin/env python

import sys, os
from math import ceil

def fill(X,R,C):
    # we must use X-ominos to fill the space. So the area must be divisible
    if ( R * C ) % X != 0:
        return False
    if X >= 7:
        # Richard can choose an X-omino that encloses a 1x1 space, which is impossible to fill
        return False

    # some special cases
    if X==1:
        # the only possible 1-omino is 1x1, which will fill any shape
        # this is already caught by the area clause
        return True
    if X==2:
        # the only possible 2-omino is 1x2. This comes down to if the shape is odd?
        # if one side is even, then it will *always* fill
        # this is already caught by the area clause
        return True
    if X==3:
        # the only possible 3-ominos are 1x3 and an L shape.
        # if the rectangular space already passes the area clause, then it must be fillable by the 1x3
        # Richard must choose the L shape
        # the only space which cannot be filled by the L shape is 1x(3N)
        if R==1 or C==1:
            return False
        else:
            return True
    if X==4:
        # Let's deal with the 1x4 4-omino:
        if R<4 and C<4:
            # Richard chooses the 1x4, and the grid cannot be filled
            return False
        else:
            # one side is 4
            if min(R,C)==1:
                # choose any shape that is 2-wide, cannot be filled
                return False
            elif min(R,C)==2:
                # 2x4 grid
                # choose T-bone, cannot be filled
                return False
            elif min(R,C)==3:
                # 3x4 grid
                # will always be filled, no matter the original choice
                return True
            else:
                # 4x4 grid
                # same with 3x4, but expand with a 1x4
                return True
          

# the first line is the total number of cases
cases_total = int(sys.stdin.readline().strip())

case = 0                                # id of the case
while case < cases_total:
    case += 1                           # iterate case id

    # do your input here
    [ X, R, C ] = [ int(x) for x in sys.stdin.readline().strip().split() ]

    # do your algorithm here
    if fill(X,R,C):
        out = "GABRIEL"
    else:
        out = "RICHARD"

    print "Case #"+str(case)+": "+out   # the output format is 'Case #${case}: ${output}'
