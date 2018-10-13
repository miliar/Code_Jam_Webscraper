#!/usr/bin/python

import sys

nextBasin = 0x61

def process(map, r, c):
    global nextBasin
    if map[r][c][1]:
        return map[r][c][1]
    
    min = map[r][c][0]
    neighR = -1
    neighC = -1
    
    if r > 0 and map[r-1][c][0] < min:
        neighR = r-1
        neighC = c
        min = map[r-1][c][0]
    
    if c > 0 and map[r][c-1][0] < min:
        neighR = r
        neighC = c-1
        min = map[r][c-1][0]
    
    if c < len(map[r])-1 and map[r][c+1][0] < min:
        neighR = r
        neighC = c+1
        min = map[r][c+1][0]
    
    if r+1 < len(map) and map[r+1][c][0] < min:
        neighR = r+1
        neighC = c
        min = map[r+1][c][0]
    
    if neighR == -1:
        map[r][c][1] = chr(nextBasin)
        nextBasin += 1
        return map[r][c][1]
    
    map[r][c][1] = process(map, neighR, neighC)
    return map[r][c][1]

def main():
    global nextBasin
    cant = int(raw_input())
    for case in xrange(1, cant+1):
        nextBasin = 0x61
        map = []
        rows, columns = raw_input().split(' ')
        rows = int(rows)
        columns = int(columns)
        for r in xrange(0, rows):
            map.append([])
            line = raw_input()
            for number in line.split(' '):
                map[r].append([int(number), ''])
        
        for r in xrange(0, rows):
            for c in xrange(0, columns):
                if map[r][c][1] == '':
                    map[r][c][1] = process(map, r, c)
        
        print "Case #" + str(case) + ":"
        for r in xrange(0, rows):
            sys.stdout.write(str(map[r][0][1]))
            for c in xrange(1,columns):
                sys.stdout.write(" " + str(map[r][c][1]))
            print ""

if __name__ == '__main__':
    main()