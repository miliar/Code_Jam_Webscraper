#!/usr/bin/env python
#
#

import sys
import re
from pprint import pprint
from array import array

DCT_SINK = 0
DCT_NORTH = 1
DCT_WEST = 2
DCT_EAST = 3
DCT_SOUTH = 4
ALTMAX = 10001

in_filename = sys.argv[1]
out_filename = '%s.out' % (in_filename,)

fin = open(in_filename)
T = int(fin.readline().strip())
print 'T=%d' % (T,)

class Maps(object):
    NORTH = 'N'
    WEST  = 'W'
    EAST  = 'E'
    SOUTH = 'S'
    SINK  = '0'
    def __init__(self, height, width, maps):
        self.height = height
        self.width = width
        self.maps = maps
    def get(self, r, c):
        try:
            if r < 0 or c < 0:
                raise IndexError
            return self.maps[r][c]
        except IndexError:
            return None
    def nwes(self, r, c):
        return (self.get(r-1, c),
                self.get(r, c-1),
                self.get(r, c+1),
                self.get(r+1, c),
                )
    def direct(self, r, c):
        cur = self.get(r, c)
        nwes = self.nwes(r,c)
        nwes_true = filter(lambda v: v is not None, nwes)
        if nwes_true:
            minval = min(nwes_true)
        else:
            return Maps.SINK
        if cur <= minval:
            return Maps.SINK
        elif nwes[0] == minval:
            return Maps.NORTH
        elif nwes[1] == minval:
            return Maps.WEST
        elif nwes[2] == minval:
            return Maps.EAST
        else:
            return Maps.SOUTH

    def letters_maps(self):
        maps = [ ['0',] * self.width for n in xrange(self.height) ]
        l = 'a'
        for y in xrange(self.height):
            for x in xrange(self.width):
                if self.setletter(l, y, x, maps):
                    l = chr(ord(l) + 1)
        return maps

    def setletter(self, l, r, c, maps):
        if maps[r][c] != '0':
            return False
        maps[r][c] = l
        d = self.direct(r, c)
        x = c
        y = r
        if d == Maps.NORTH:  y -= 1
        elif d == Maps.WEST: x -= 1
        elif d == Maps.EAST: x += 1
        elif d == Maps.SOUTH: y += 1
        self.setletter(l, y, x, maps)

        y = r - 1
        x = c
        if self.direct(y, x) == Maps.SOUTH:
            self.setletter(l, y, x, maps)
        y = r
        x = c - 1
        if self.direct(y, x) == Maps.EAST:
            self.setletter(l, y, x, maps)
        y = r
        x = c + 1
        if self.direct(y, x) == Maps.WEST:
            self.setletter(l, y, x, maps)
        y = r + 1
        x = c
        if self.direct(y, x) == Maps.NORTH:
            self.setletter(l, y, x, maps)
        return True

fout = open(out_filename, 'w')
for m in xrange(T):
    H, W = map(int, re.split(r'\s', fin.readline().strip()))
    print 'H=%d, W=%d' % (H, W)

    maps = []
    for n in xrange(H):
       maps.append(re.split(r'\s', fin.readline().strip()))
    mymaps = Maps(H, W, maps)

    print 'maps'
    for h in xrange(H):
        for w in xrange(W):
            print('%s' % mymaps.get(h, w)),
        print ''

    print 'maps_direct'
    for h in xrange(H):
        for w in xrange(W):
            print('%s' % mymaps.direct(h, w)),
        print ''

    print 'letters'
    maps = mymaps.letters_maps()
    for h in xrange(H):
        for w in xrange(W):
            print('%s' % maps[h][w]),
        print ''

    fout.write("Case #%d:\n" % (m+1,))
    for h in xrange(H):
        fout.write(" ".join(map(str, maps[h])))
        fout.write("\n")

#
# EOF
#
