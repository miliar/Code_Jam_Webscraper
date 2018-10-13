#!/usr/bin/env python

import sys, string

def checkSink(elevations,h,w):
    if ( h == 0 or elevations[h][w] <= elevations[h-1][w] ):
        if (w == 0 or elevations[h][w] <= elevations[h][w-1] ):
            if ( h == len(elevations) - 1 or elevations[h][w] <= elevations[h+1][w] ):
                if ( w == len(elevations[h]) - 1 or elevations[h][w] <= elevations[h][w+1] ):
                    return True
    return False

def expandSinkUp(elevations,sinks,h,w,sink):
    if sinks[h][w]:
        return
    if ( elevations[h+1][w] < elevations[h][w] ):
        if ( w == len(elevations[h]) - 1 or elevations[h+1][w] < elevations[h][w+1] ):
            if ( h == 0 or elevations[h+1][w] < elevations[h-1][w] ):
                if ( w == 0 or elevations[h+1][w] < elevations[h][w-1] ):
                    sinks[h][w] = sink
                    if h != 0: 
                        expandSinkUp(elevations,sinks,h-1,w,sink)
                    if w != 0: 
                        expandSinkLeft(elevations,sinks,h,w-1,sink)
                    if w != len(elevations[h]) - 1: 
                        expandSinkRight(elevations,sinks,h,w+1,sink)

def expandSinkDown(elevations,sinks,h,w,sink):
    if sinks[h][w]:
        return
    if ( elevations[h-1][w] < elevations[h][w] ):
        if ( w == len(elevations[h]) - 1 or elevations[h-1][w] <= elevations[h][w+1] ):
            if ( h == len(elevations) - 1 or elevations[h-1][w] <= elevations[h+1][w] ):
                if ( w == 0 or elevations[h-1][w] <= elevations[h][w-1] ):
                    sinks[h][w] = sink
                    if h != len(elevations) - 1: 
                        expandSinkDown(elevations,sinks,h+1,w,sink)
                    if w != 0: 
                        expandSinkLeft(elevations,sinks,h,w-1,sink)
                    if w != len(elevations[h]) - 1: 
                        expandSinkRight(elevations,sinks,h,w+1,sink)

def expandSinkLeft(elevations,sinks,h,w,sink):
    if sinks[h][w]:
        return
    if ( elevations[h][w+1] < elevations[h][w] ):
        if ( h == 0 or elevations[h][w+1] < elevations[h-1][w] ):
            if ( h == len(elevations) - 1 or elevations[h][w+1] <= elevations[h+1][w] ):
                if ( w == 0 or elevations[h][w+1] < elevations[h][w-1] ):
                    sinks[h][w] = sink
                    if h != len(elevations) - 1: 
                        expandSinkDown(elevations,sinks,h+1,w,sink)
                    if w != 0: 
                        expandSinkLeft(elevations,sinks,h,w-1,sink)
                    if h != 0: 
                        expandSinkUp(elevations,sinks,h-1,w,sink)

def expandSinkRight(elevations,sinks,h,w,sink):
    if sinks[h][w]:
        return
    if ( elevations[h][w-1] < elevations[h][w] ):
        if ( h == 0 or elevations[h][w-1] < elevations[h-1][w] ):
            if ( h == len(elevations) - 1 or elevations[h][w-1] <= elevations[h+1][w] ):
                if ( w == len(elevations[h]) - 1 or elevations[h][w-1] <= elevations[h][w+1] ):
                    sinks[h][w] = sink
                    if h != len(elevations) - 1: 
                        expandSinkDown(elevations,sinks,h+1,w,sink)
                    if w != len(elevations[h]) - 1: 
                        expandSinkRight(elevations,sinks,h,w+1,sink)
                    if h != 0: 
                        expandSinkUp(elevations,sinks,h-1,w,sink)

n = int(sys.stdin.readline().strip())

for i in range(n):
    elevations = []
    sinks = []
    dimensions = sys.stdin.readline().strip().split(" ")
    height = int(dimensions[0])
    width = int(dimensions[1])
    for j in range(height):
        elevations.append([])
        sinks.append([])
        input = sys.stdin.readline().strip().split(" ")
        for k in range(width):
            elevations[j].append(int(input[k]))
            sinks[j].append("")

    num = 0
    for j in range(height):
        for k in range(width):
            found = checkSink(elevations,j,k)
            if (not sinks[j][k]) and found:
                thisSink = string.lowercase[num]
                num += 1
                sinks[j][k] = thisSink
                if j != len(elevations) - 1:
                    expandSinkDown(elevations,sinks,j+1,k,thisSink)
                if j != 0:
                    expandSinkUp(elevations,sinks,j-1,k,thisSink)
                if k != len(elevations[j]) - 1:
                    expandSinkRight(elevations,sinks,j,k+1,thisSink)     
                if k != 0:
                    expandSinkLeft(elevations,sinks,j,k-1,thisSink)  

    map = {}
    num = 0
    for j in range(height):
        for k in range(width):
            if sinks[j][k] not in map.keys():
                map[sinks[j][k]] = string.lowercase[num]
                num += 1
            sinks[j][k] = map[sinks[j][k]]

    print "Case #%d:" % (i+1)
    for j in range(height):
        print " ".join(sinks[j])

