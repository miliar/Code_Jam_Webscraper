#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def flip(cakes, idx, flipSize):
    flipCakes = ""
    for i in range(len(cakes)):
        if i > idx-flipSize and i <= idx:
            flipCakes += "+" if cakes[i] == "-" else "-"
        else:
            flipCakes += cakes[i]
    return flipCakes

def solve(case, cakes, fSize):
    flipTimes = 0

    for i in range(len(cakes)-fSize+1):
        idx = i + fSize - 1
        if cakes[idx-fSize+1] == "-":
            cakes = flip(cakes, idx, fSize)
            flipTimes += 1

    if "-" in cakes:
        return "Case #%d: IMPOSSIBLE\n" % (case)
    else:
        return "Case #%d: %d\n" % (case, flipTimes)

if __name__ == "__main__":
    isFirst = True
    totalCase = 0
    currentCase = 1

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue

        # execute
        out = solve(currentCase, items[0], int(items[1]))
        outFile.write(out)
        print out.rstrip()

        # go next
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break

