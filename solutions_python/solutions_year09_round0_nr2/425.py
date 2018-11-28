#!/usr/bin/env python
import sys

t = int(sys.stdin.readline())

for mapIx in xrange(t):
    #print "processing map %d"%mapIx
    h,w = tuple(map(int,sys.stdin.readline().split(" ")))
    #print "h,w: %s"%[h,w]
    rows = []
    for i in xrange(h):
        rows += [map(int,sys.stdin.readline().split(" "))]
    #print "rows: %s"%rows
    
    basins = [[[(i,j)] for j in xrange(w)] for i in xrange(h)] 
    #print "basins: %s"%basins
    
    for i in xrange(h):
        for j in xrange(w):
            drainsTo = None
            altitude = rows[i][j]
            if i>0:
                if rows[i-1][j] < altitude:
                    drainsTo = (i-1, j)
                    altitude = rows[i-1][j]
            if j>0:
                if rows[i][j-1] < altitude:
                    drainsTo = (i,j-1)
                    altitude = rows[i][j-1]
            if j<w-1:
                if rows[i][j+1] < altitude:
                    drainsTo = (i,j+1)
                    altitude = rows[i][j+1]
            if i<h-1:
                if rows[i+1][j] < altitude:
                    drainsTo = (i+1, j)
                    altitude = rows[i+1][j]
            if drainsTo != None:
                newBasin = basins[i][j] + basins[drainsTo[0]][drainsTo[1]]
                #print "%s newBasin: %s" % ([i,j],newBasin)
                for (i1,j1) in newBasin:
                    basins[i1][j1] = newBasin
            #else:
                #print "sink found! %s"%[i,j]
    
    #print "computed basins: %s" %basins
    letters = {}
    letter = ord('a')
    print "Case #%d:"%(mapIx+1)
    for i in xrange(h):
        for j in xrange(w):
            if str(basins[i][j]) not in letters:
                letters[str(basins[i][j])] = chr(letter)
                letter += 1
            print letters[str(basins[i][j])],
            if j < w-1:
                pass #print " ",
            else:
                print ""

