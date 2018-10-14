from __future__ import division, print_function
import string
import re

def cjw(fInP="in.txt", fOutP="out.txt"):
    def flowDir (x, y):
        if (x<0 or x>=W or y<0 or y>=H or reg[y][x]):
            return "X"
        fDir = "X"
        lowest = alt(x, y)
        altN = alt(x, y-1)
        if (altN < lowest):
            fDir = "N"
            lowest = altN
        altN = alt(x-1, y)
        if (altN < lowest):
            fDir = "W"
            lowest = altN 
        altN = alt(x+1, y)
        if (altN < lowest):
            fDir = "E"
            lowest = altN 
        altN = alt(x, y+1)
        if (altN < lowest):
            fDir = "S"
            lowest = altN
        return fDir
    
    def update (x, y, r):
        if (reg[y][x]):
            return
        fdir = flowDir(x, y)
        reg[y][x] = r
        fdirN = flowDir(x, y-1)
        if (fdir == "N" or fdirN == "S"):
            update (x, y-1, r)
        fdirN = flowDir(x-1, y)
        if (fdir == "W" or fdirN == "E"):
            update (x-1, y, r)
        fdirN = flowDir(x+1, y)
        if (fdir == "E" or fdirN == "W"):
            update (x+1, y, r)
        fdirN = flowDir(x, y+1)
        if (fdir == "S" or fdirN == "N"):
            update (x, y+1, r)
    
    def alt (x, y):
        if (x<0 or x>=W or y<0 or y>=H):
            return 100000
        return mapA[y][x]
    
    fIn = open(fInP, 'r')
    fOut = open(fOutP, 'w')
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    N = int(fIn.readline())
    for n in range(0, N):
        fOut.write('Case #' + str(n+1) + ':\n')
        H, W = (int(x) for x in fIn.readline().split())
        mapA = []
        #read map
        for row in range(0, H):
            altitude = [int(altitude) for altitude in fIn.readline().split()]
            mapA.append (altitude)
        #code
        countR = 1
        reg = [[0 for i in range(0, W)] for j in range(0, H)]
        for j in range(0, H):
            line = ""
            for i in range(0, W):
                if (reg[j][i] == 0):
                    update(i, j, countR)
                    countR+=1
                line += alphabet[reg[j][i]-1]
                if (i < W-1):
                    line += " "
            fOut.write(line + '\n')

