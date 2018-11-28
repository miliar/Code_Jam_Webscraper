#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys

number_of_maps = int(sys.stdin.readline())

NORTH = 1
WEST = 2
EAST = 3
SOUTH = 4

def chargen():
    base = ord('a')
    while True:
        yield base
        base += 1

for caseno in xrange(number_of_maps):
    height, width = map(int, sys.stdin.readline().split())

    alt = []
    for row in xrange(height):
        tmp = map(int, sys.stdin.readline().split())
        assert len(tmp) == width
        alt.append(tmp)
    # alt[row][col] ~ m[y][x]
    graph = [ [set() for x in xrange(width)] for y in xrange(height)]
    def add_edge(a, b):
        """ a ~ (row, col) """
        graph[a[0]][a[1]].add(b)
        graph[b[0]][b[1]].add(a)

    for row in xrange(height):
        for col in xrange(width):
            tocheck = []
            if row-1 >= 0:
                tocheck.append( (alt[row-1][col], NORTH, (row-1, col)) )
            if row+1 < height:
                tocheck.append( (alt[row+1][col], SOUTH, (row+1, col)) )
            if col-1 >= 0:
                tocheck.append( (alt[row][col-1], WEST, (row, col-1)) )
            if col+1 < width:
                tocheck.append( (alt[row][col+1], EAST, (row, col+1)) )
            if tocheck:
                neighb_alt, direction, neighb_coord = min(tocheck)
                if neighb_alt < alt[row][col]:
                    add_edge( (row, col),  neighb_coord )

    char = chargen()
    result = [ [None for x in xrange(width)] for y in xrange(height)]

    def flood_fill(row, col):
        curchar = result[row][col]
        for neirow, neicol in graph[row][col]:
            if result[neirow][neicol] is None:
                result[neirow][neicol] = curchar
                flood_fill(neirow, neicol)

    for row in xrange(height):
        for col in xrange(width):
            if result[row][col] is None:
                result[row][col] = char.next()
            flood_fill(row, col)

    print 'Case #%i:' % (caseno+1)
    for row in result:
        print ' '.join(map(chr, row))

# vim:set tabstop=4 softtabstop=4 shiftwidth=4 expandtab: 
