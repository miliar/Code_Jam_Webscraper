#!/usr/bin/python

import sys
import re

def getNorth(map, y, x):
    y = y - 1
    if y < 0:
       return sys.maxint
    return map[y][x]

def getSouth(map, y, x):
    y = y + 1
    if y >= len(map):
       return sys.maxint
    return map[y][x]

def getEast(map, y, x):
    x = x + 1
    if x >= len(map[0]):
       return sys.maxint
    return map[y][x]

def getWest(map, y, x):
    x = x - 1
    if x < 0:
       return sys.maxint
    return map[y][x]

filename = sys.argv[1]
file = open(filename, 'r')
numMaps = int(file.readline())
# print numMaps, 'map(s)'

for mapNumber in range(numMaps):
    height, width = tuple(file.readline().strip().split(' '))
    height = int(height)
    width = int(width)
    # print width, 'x', height

    map = []
    for line in range(height):
        row = []
        for column in file.readline().strip().split(' '):
            row.append(int(column))
        map.append(row)

    # print 'Map:'
    # for row in map:
    #     print ' '.join([str(i) for i in row])

    flow = []
    for i in range(len(map)):
        flowRow = []

        for j in range(len(map[0])):
            north = getNorth(map, i, j)
            west = getWest(map, i, j)
            east = getEast(map, i, j)
            south = getSouth(map, i, j)

            minAltitude = min(north, west, east, south)
            currentAltitude = map[i][j]

            if currentAltitude <= minAltitude:
                flowRow.append(None)
            else:
                if north == minAltitude:
                    flowRow.append([i - 1, j])
                elif west == minAltitude:
                    flowRow.append([i, j - 1])
                elif east == minAltitude:
                    flowRow.append([i, j + 1])
                elif south == minAltitude:
                    flowRow.append([i + 1, j])
                else:
                    print "THIS SHOULD NOT HAPPEN"

        flow.append(flowRow)

    # print 'Flow:'
    # for row in flow:
    #     print ' '.join([str(i) for i in row])

    basinLetter = 'a'
    basins = []
    for row in range(len(flow)):
        basins.append([])
        for col in range(len(flow[0])):
            basins[row].append(None)

    for i in range(len(flow)):
        for j in range(len(flow[0])):
            k, l = i, j

            while flow[k][l] != None:
                k, l = tuple(flow[k][l])

            if basins[k][l] != None:
                basins[i][j] = basins[k][l]
            else:
                basins[i][j] = basinLetter
                basins[k][l] = basinLetter
                basinLetter = chr(ord(basinLetter) + 1)

    print 'Case #' + str(mapNumber + 1) + ':'
    for row in basins:
        print ' '.join([str(i) for i in row])

file.close()
