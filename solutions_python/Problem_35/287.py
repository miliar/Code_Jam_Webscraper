#!/usr/bin/env python

import sys
import string
import re

class Element(object):
    def __init__(self, altitude):
        self.altitude = altitude
        self.explored = False
        self.fathers = set()
        self.son = None
        self.directions = [None, None, None, None] #NWES
        self.basin = None
    
    def explore(self, father):
        if father != None:
            self.fathers.add(father)
        if self.explored:
            return
        self.explored = True
        minIdx = -1
        for i in range(4):
            if self.directions[i] is not None:
                if minIdx == -1:
                    minIdx = i
                elif self.directions[i].altitude < self.directions[minIdx].altitude:
                    minIdx = i
        if minIdx != -1 and self.directions[minIdx].altitude < self.altitude:
            self.son = self.directions[minIdx]
            self.son.explore(self)
    
    def markBasin(self, letter):
        if self.basin != None:
            return False
        self.basin = letter
        if self.son:
            self.son.markBasin(letter)
        for father in self.fathers:
            father.markBasin(letter)
        return True
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <dataset_name>" % sys.argv[0]
        sys.exit(1)
    
    inFile = open(sys.argv[1] + ".in", "r")
    lines = map(lambda x: x[:-1], inFile.readlines())
    inFile.close()
    
    T = int(lines[0])
    del lines[0]
    
    maps = []
    for i in range(T):
        (H, W) = map(int, lines[0].split(" "))
        aMap = []
        for j in range(H):
            aMap.append(map(lambda x: Element(int(x)), lines[j+1].split(" ")))
        for h in range(H):
            for w in range(W):
                if h != 0:
                    aMap[h][w].directions[0] = aMap[h-1][w]
                if w != 0:
                    aMap[h][w].directions[1] = aMap[h][w-1]
                if w != W - 1:
                    aMap[h][w].directions[2] = aMap[h][w+1]
                if h != H - 1:
                    aMap[h][w].directions[3] = aMap[h+1][w]
        maps.append(aMap)
        lines = lines[1+H:]
    
    for m in maps:
        for line in m:
            for item in line:
                item.explore(None)
    
    letters = 'abcdefghijklmnopqrstuvwxyz0'
    for m in maps:
        idx = 0
        for line in m:
            for item in line:
                if item.markBasin(letters[idx]):
                    idx += 1
    
    outFile = open(sys.argv[1] + ".out", "w")
    for i in range(len(maps)):
        outFile.write("Case #%d:\n" % (i + 1))
        for row in maps[i]:
            outFile.write("%s\n" % " ".join(map(lambda x: x.basin if x.basin else '.', row)))
    outFile.close()