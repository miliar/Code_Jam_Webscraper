from itertools import *
import pickle

infile = "A-large (1).in"

lines = [s.rstrip() for s in open(infile, "rb").readlines()]
NCases=int(lines[0])

def make_red(tiles, m, n):
    if (tiles[m+1][n] != "#" or tiles[m+1][n+1] != "#" or tiles[m][n+1] != "#"):
        raise Exception ("err")
    tiles[m][n] = "/"
    tiles[m+1][n] = "\\"
    tiles[m][n+1] = "\\"
    tiles[m+1][n+1] = "/"

def pave(tiles, rows, cols):
    try:
        for m in range(rows):
            for n in range(cols):
                if (tiles[m][n] == "#"):
                    make_red(tiles, m, n)
        return (True)
    except:
        return (False)
                

pos = 1
for i in range(NCases):
    Nrows, Ncolumns = [int(c) for c in lines[pos].split(" ")]
    tiles = []
    for ti in range(Nrows):
        #tiles_m = []
        #scores = lines[pos + ti + 1]
        #for m, sc in range(Ncolumns):
        tiles.append(list(lines[pos + ti + 1]))
    #print tiles
    pos += Nrows + 1
    res = pave(tiles, Nrows, Ncolumns)
    if (not res):
        str = "Impossible"
    else:
        str = "\r\n".join(["".join(row) for row in tiles])
    print "Case #%d:\n%s" % (i+1, str)
    #for ti in range(Nteams):
    #    print RPI (matches, ti)
    
