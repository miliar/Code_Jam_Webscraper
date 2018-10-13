#!/bin/python


def getTime (items):
    sortedItems = sorted(items)
    outOfOrder = 0
    for i in range(len(items)):
        if sortedItems[i] != items[i]:
            outOfOrder += 1
    return outOfOrder


def main ():
    input = open("input.txt")
    testcases = int(input.readline())
    
    lineNumber = 0
    for line in input:
        lineNumber += 1
        if lineNumber % 2 == 1: continue
        case = lineNumber / 2
        items = [int(i) for i in line.strip().split(" ")]
        time = getTime(items)
        print "Case #%d: %d" % (case, time)


if __name__ == "__main__": main()