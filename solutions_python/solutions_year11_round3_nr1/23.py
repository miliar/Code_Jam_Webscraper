#!/usr/bin/python


def cread(fd):
    return fd.readline().strip('\n')


BLUE = "#"

RED = "/\\"

def solve(fd):

    R, C = [ int(x) for x in cread(fd).split() ]

    Tiles = [None]*R
    for i in xrange(R):
        Tiles[i] = list(cread(fd))

    # Lests go row by row
    for i in xrange(R):
        for j in xrange(C):
            if Tiles[i][j]==BLUE:
                # Cover it!
                if i==R-1 or j==C-1:
                    # We are at a border :(
                    return None
                if ( Tiles[i][j+1]!=BLUE or
                     Tiles[i+1][j]!=BLUE or
                     Tiles[i+1][j+1]!=BLUE):
                    return None
                Tiles[i][j] = "/"
                Tiles[i][j+1] = "\\"
                Tiles[i+1][j] = "\\"
                Tiles[i+1][j+1] = "/"
    return Tiles


import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(cread(fd))

for i in xrange(T):
    sol = solve(fd)
    if sol is None:
        txt = "\nImpossible"
    else:
        txt = ""
        for row in sol:
            txt += "\n" + ''.join(row)
    print("Case #%d:" % (i+1) + txt)
    
fd.close()
    
    
