#!/usr/bin/env python

class UnionFind:
    def __init__(self):
        self.parent = self

    def find(self):
        if self.parent == self:
            return self
        else:
            parent = self.parent.find()
            return parent

    def union(self, other):
        self.find().parent = other.find()

def solve(elev):
    uf = [ [ UnionFind() for _ in row ] for row in elev ]
    for y in range(len(elev)):
        for x in range(len(elev[0])):
            minheight = elev[y][x]
            for ny, nx in [ (y-1, x), (y, x-1), (y, x+1), (y+1, x) ]:
                if 0 <= ny < len(elev) and 0 <= nx < len(elev[0]):
                    if elev[ny][nx] < minheight:
                        minheight = elev[ny][nx]
            if minheight == elev[y][x]: 
                continue
            for ny, nx in [ (y-1, x), (y, x-1), (y, x+1), (y+1, x) ]:
                if 0 <= ny < len(elev) and 0 <= nx < len(elev[0]):
                    if elev[ny][nx] == minheight:
                        uf[y][x].union(uf[ny][nx])
                        break
    
    names = list("abcdefghijklmnopqrstuvwxyz")
    names.reverse()

    basins = {}
    answer = [ [ "?" for _ in row ] for row in elev ]
    for y in range(len(elev)):
        for x in range(len(elev[0])):
            b = uf[y][x].find()
            if b not in basins:
                basins[b] = names.pop()
            answer[y][x] = basins[b]
    return answer
            

import sys
for i in range(int(sys.stdin.readline())):
    print "Case #%d:" % (i+1)
    h,w = map(int, sys.stdin.readline().split())
    
    heights = [ [ int(x) for x in sys.stdin.readline().split() ] for _ in range(h) ]
    basins = solve(heights)

    for row in basins:
        for column in row:
            print column,
        print
