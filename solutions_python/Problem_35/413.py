#! /usr/bin/env python

import sys

class Cell :
    def __init__(self, alt) :
        self.alt = alt
        self.sink = None
        self.sources = []
        self.basin = ''

    def __str__(self) :
        return self.basin

    def addSource(self, src) :
        if ( src.sink ) : src.sink.sources.remove(src)
        src.sink = self
        self.sources.append(src)

    def setBasin(self, basin) :
        self.basin = basin
        if ( self.sink and not self.sink.basin ) :
            self.sink.setBasin(basin)
        for s in self.sources :
            if ( not s.basin ) :
                s.setBasin(basin)


class Map :
    def __init__(self) :
        self.cells = []

    def display(self) :
        for i in self.cells :
            for j in i :
                print j,
            print ""

    def addCell(self, alt, row, col) :
        c = Cell(alt)
        nNorth = nWest = None
        if ( row ) :
            nNorth = self.cells[row - 1][col]
            if ( (nNorth.sink and alt < nNorth.sink.alt) or ((not nNorth.sink) and alt < nNorth.alt) ) :
                c.addSource(nNorth)

        if ( col ) :
            self.cells[row].append(c)
            nWest = self.cells[row][col - 1]
            if ( (nWest.sink and alt < nWest.sink.alt) or ((not nWest.sink) and alt < nWest.alt) ) :
                c.addSource(nWest)
        else :
            self.cells.append([c])

        if ( nNorth or nWest ) :
            if ( nNorth and nWest ) :
                if ( len(c.sources) < 2 ) :
                    if ( nWest.alt < nNorth.alt ) :
                        if ( nWest.alt < alt ) :
                            nWest.addSource(c)
                    else :
                        if ( nNorth.alt < alt ) :
                            nNorth.addSource(c)
            elif ( nNorth ) :
                if ( nNorth.alt < alt ) :
                    nNorth.addSource(c)
            else :
                if ( nWest.alt < alt ) :
                    nWest.addSource(c)

    def setBasins(self) :
        basin = ord('a')
        for i in self.cells :
            for j in i :
                if ( not j.basin ) :
                    j.setBasin(chr(basin))
                    basin += 1



if ( len(sys.argv) > 1 ) :
    file = open(sys.argv[1], "r")
else :
    file = sys.stdin

T = int(file.readline().rstrip())

for i in range(1, T + 1) :
    map = Map()
    H, W = [int(n) for n in file.readline().rstrip().split()]
    for rn in range(H) :
        row = [int(a) for a in file.readline().rstrip().split()]
        for cn in range(W) :
            map.addCell(row[cn], rn, cn)

    map.setBasins()
    print 'Case #' + str(i) + ':'
    map.display()
    del map

