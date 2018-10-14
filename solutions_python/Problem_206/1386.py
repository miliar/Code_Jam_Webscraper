#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")


def solve(case, Dest, values):
    longestTravelTime = -1
    for i in range(len(values)):
        pos = values[i][0]
        speed = values[i][1]
        remainLoad = Dest - pos
        travelTime = remainLoad / float(speed)
        if longestTravelTime < travelTime:
            longestTravelTime = travelTime
    answer = Dest / longestTravelTime
    return "Case #%d: %.6f\n" % (case, answer)

if __name__ == "__main__":
    isFirst = True
    inData = False

    totalCase = 0
    currentCase = 1

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue

        if inData == False:
            Dest = int(items[0])
            NumOfHourse = int(items[1])
            inData = True
            rowIndex = 0
            values = []
        else:
            rowIndex = rowIndex + 1
            values.append([int(items[0]), int(items[1])])

            if rowIndex == NumOfHourse:
                out = solve(currentCase, Dest, values)
                outFile.write(out)
                print out.rstrip()
                inData = False
                rowIndex = 0
                values = []

                # go next
                currentCase = currentCase + 1
                if currentCase > totalCase:
                    break

