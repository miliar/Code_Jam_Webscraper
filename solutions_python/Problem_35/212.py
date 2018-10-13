#!/usr/bin/env python

import sys

def line():
    return sys.stdin.readline()[:-1]

def basins(terrain,H,W):
    minimum = terrain[(0,0)]
    result = []
    for row in range(H):
        for col in range(W):
            if terrain[(row,col)] < minimum:
                minimum = terrain[(row,col)]
                result = [(row,col)]
            elif terrain[(row,col)] == minimum:
                result.append((row,col))
    return result

def dest(terrain,row,col,H,W):
    minimum = terrain[(row,col)]
    result = (row,col)
    for (r,c) in neighbors(row,col,H,W):
        if terrain[(r,c)] < minimum:
            result = (r,c)
            minimum = terrain[(r,c)]
    return result

def neighbors(row,col,H,W):
    candidates = [(row-1,col),(row,col-1),(row,col+1),(row+1,col)]
    candidates = [(row,col) for (row,col) in candidates if row >= 0 and row < H and col >= 0 and col < W]
    return candidates

if __name__ == "__main__":
    T = eval(line())
    for caseNumber in range(1,T+1):
        H,W = map(eval,line().split())
        terrain = dict()
        drainage = dict()
        for row in range(H):
            cols = map(eval,line().split())
            for col in range(W):
                terrain[(row,col)] = cols[col]
                drainage[(row,col)] = None
        # We reverse the dest function
        drainsTo = dict()
        for row in range(H):
            for col in range(W):
                destination = dest(terrain,row,col,H,W)
                if destination not in drainsTo:
                    drainsTo[destination] = []
                drainsTo[destination].append((row,col))
        # We propagate basin assignments
        for (row,col) in basins(terrain,H,W):
            drainage[(row,col)] = (row,col)
            toVisit = drainsTo[(row,col)]
            while len(toVisit) != 0:
                newDest = toVisit.pop(0)
                drainage[newDest] = (row,col)
                if newDest in drainsTo:
                    toVisit.extend(drainsTo[newDest])
        # We translate basin coordinates into letter
        translation = dict()
        for row in range(H):
            for col in range(W):
                if drainage[(row,col)] not in translation:
                    translation[drainage[(row,col)]] = chr(len(translation) + ord('a'))
                drainage[(row,col)] = translation[drainage[(row,col)]]
        print "Case #" + str(caseNumber) + ":"
        for row in range(H):
            print ' '.join([drainage[(row,col)] for col in range(W)])

