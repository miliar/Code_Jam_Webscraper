#! /usr/bin/env python
from copy import deepcopy

def main():
    maxheight = 100
    lawns = []
    numLawns = int(raw_input())
    for i in xrange(numLawns):
        currLawn = []
        length = int(raw_input().split(' ')[0])
        for j in xrange(length):
            currLawn.append([int(num) for num in raw_input().split(' ')])
        lawns.append(currLawn)

    i = 0
    for lawn in lawns:
        i += 1
        if mowable(lawn, maxheight):
            print "Case #" + str(i) + ": YES"
        else:
            print "Case #" + str(i) + ": NO"

def mowable(target, maxheight):
    lawn = [[maxheight for column in target[0]] for row in target]
    while True:
        newLawn = deepcopy(lawn)
        newLawn = mow(newLawn, target)
        if isEqual(newLawn, lawn):
            break
        lawn = newLawn
    if isEqual(lawn, target):
        return True
    return False

def isEqual(oldLawn, newLawn):
    for i in xrange(len(oldLawn)):
        for j in xrange(len(oldLawn[0])):
            if oldLawn[i][j] != newLawn[i][j]:
                return False
    return True

def mow(lawn, target):
    # Mow horizontally
    for row in xrange(len(lawn)):
        height = rowHigh(target[row])
        lawn[row] = [min(height,point) for point in lawn[row]]
    # Now the harder vertical mowing
    for column in xrange(len(lawn[0])):
        targetColumn = [target[row][column] for row in xrange(len(target))]
        height = rowHigh(targetColumn)
        for row in xrange(len(lawn)):
            lawn[row][column] = min(height, lawn[row][column])
    return lawn

def rowHigh(row):
    high = 0
    for point in row:
        if point > high:
            high = point
    return high

if __name__=="__main__":
    main()