#!/usr/bin/python

import sys

class Map:
    def __init__(self,H,W):
        self.altitudes = []
        self.table = []
        self.H = H
        self.W = W
    
    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.table])

    def add_row(self,row):
        """ must add as we read them in"""
        self.altitudes.append([int(x) for x in row.split()])
        self.table.append( [""] * self.W)

    def downmost(self,i,j):
        """ return the first coordpair in options with a lower altitude than (i,j)
        if none are lower return (i,j)
        """
        start = (i,j)
        options = [start]
        if 1 <= i:
            options.append((i-1,j)) # north
        if 1 <= j:
            options.append((i,j-1)) # west
        if j < self.W-1:
            options.append((i,j+1)) # east
        if i < self.H-1:
            options.append((i+1,j)) # south
        alt = self.altitudes[i][j]
        lowest = start
###        print ' '.join([ "%s:%d" % (str(op),(self.altitudes[op[0]][op[1]])) for op in options])
        for (x,y) in options[::-1]: # read backwards
            if self.altitudes[x][y] <= alt:
                alt = self.altitudes[x][y]
                lowest = (x,y)
        return lowest



    def rain(self,i,j,label):
        """
        path = []
        while current position is unmarked:
            path.append (current)
            next = downmost(current)
            if next == current then we are at a sink:
                if sink is unmarked:
                    label++
                    mark sink
        get label of current and paint path
        """
        if self.table[i][j]:
            return label
        path = []
        current = (i,j)
###        print "make it rain", current
        while True:
            path.append(current)
            next = self.downmost(current[0],current[1])
###            print "moving from ",current,"to",next
            if next == current:
                if self.table[current[0]][current[1]]:
                    basin_name = self.table[current[0]][current[1]]
###                    print "found a sink with a label"
                    break
###                print "found a sink WITHOUT a label"
                basin_name = chr(ord(label)+1)
###                print self
                break
            current = next
###        print path, basin_name
        for (x,y) in path:
            self.table[x][y] = basin_name
        return basin_name

    
    def forty_days(self):
        i = 0 #column index
        j = 0 # row index
        label = self.rain(i,j,chr(ord("a")-1))
        while True:
            if j < W and i < H:
                label = self.rain(i,j,label)
                j += 1
            if j >= W:
                j = 0
                i += 1
            if i >= H:
                break


            


T = int(sys.stdin.readline()) # number of maps

for i in xrange(T):
    print "Case #%d:" % (i+1)
    H, W = [int(n) for n in sys.stdin.readline().split()]
    m = Map(H,W)
    for i in xrange(H):
        # i = 0 is north, i = H is southern most row
        m.add_row(sys.stdin.readline())

    m.forty_days() # make it rain
###    print "test:"
###    print '\n'.join([' '.join([str(n) for n in row]) for row in m.altitudes])
    print m
        

