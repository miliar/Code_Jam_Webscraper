#!/usr/bin/python
import sys

# Some constants
NORTH = 0
WEST  = 1
EAST  = 2
SOUTH = 3
SINK  = 4

alphabet = [chr(x) for x in xrange(ord('a'), ord('z')+1)]

class Map_MFSet:
    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.data=[i for i in xrange(W*H)]
        self.reps=dict( [(i,None) for i in xrange(W*H)] )

    def point2pos(self, p):
        x,y=p
        return self.W*y + x

    def find(self, p):
        pos = self.point2pos(p)
        parent = self.data[pos]
        while pos != parent:
            pos = parent
            parent = self.data[pos]
        return pos

    # ORDER IS IMPORTANT
    def merge(self, p1, p2):
        pos1 = self.find(p1)
        pos2 = self.find(p2)
        if pos1 < pos2:
            self.data[pos2] = pos1
            if pos2 in self.reps:
                del self.reps[pos2]
        else:
            self.data[pos1] = pos2
            if pos1 in self.reps:
                del self.reps[pos1]

class Map:
    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.data = [0] * (W*H)

    def get(self, x, y):
        if x<0 or x>=self.W or y<0 or y>=self.H:
            return sys.maxint # kind of an "infinite" value here :)
        return self.data[self.W*y+x]

    def set(self, x, y, value):
        self.data[self.W*y+x] = value


######### MAIN PROGRAM ###########

T = input()

for map_nr in range(T):
    H,W = [int(x) for x in raw_input().split()]
    mfset = Map_MFSet(W,H)
    # read map
    map = Map(W, H)
    for y in xrange(H):
        row = [int(x) for x in raw_input().split()]
        for x in xrange(W):
            map.set(x,y,row[x])

    # merge connected components
    for y in xrange(H):
        for x in xrange(W):
            # get neighbor heights
            h = map.get(x,y)
            north = map.get(x, y-1)
            west  = map.get(x-1, y)
            east  = map.get(x+1, y)
            south = map.get(x, y+1)
            
            # get water flow direction
            lowest = h
            direction = SINK
            if north < lowest:
                lowest = north
                direction = NORTH
            if west < lowest:
                lowest = west
                direction = WEST
            if east < lowest:
                lowest = east
                direction = EAST
            if south < lowest:
                lowest = south
                direction = SOUTH

            # merge following flow direction (if not sink, of course)
            if direction == NORTH:
                mfset.merge((x,y), (x,y-1))
            elif direction == WEST:
                mfset.merge((x,y), (x-1,y))
            elif direction == EAST:
                mfset.merge((x,y), (x+1,y))
            elif direction == SOUTH:
                mfset.merge((x,y), (x,y+1))

    # get representatives and print map
    reps = mfset.reps.keys()
    reps.sort()
    translation = dict(zip(reps, alphabet))

    print "Case #%d:"%(map_nr+1)
    for y in range(H):
        for x in range(W-1):
            sys.stdout.write("%c "%translation[mfset.find((x,y))])
        sys.stdout.write("%c\n"%translation[mfset.find((W-1, y))])

    

