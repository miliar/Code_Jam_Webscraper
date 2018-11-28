#!/usr/bin/python
import sys

fileName = sys.argv[1]

f = open(fileName, "r")
a = open(fileName + "-answer", "w")

lines = f.read().split("\n")
cases = int(lines.pop(0))
for case in range(1,cases+1):
    firstAnswer  = int(lines.pop(0)) - 1
    firstSetup = list()
    firstSetup.append(map(int, lines.pop(0).split(" ")))
    firstSetup.append(map(int, lines.pop(0).split(" ")))
    firstSetup.append(map(int, lines.pop(0).split(" ")))
    firstSetup.append(map(int, lines.pop(0).split(" ")))

    nextAnswer  = int(lines.pop(0)) - 1
    nextSetup = list()
    nextSetup.append(map(int, lines.pop(0).split(" ")))
    nextSetup.append(map(int, lines.pop(0).split(" ")))
    nextSetup.append(map(int, lines.pop(0).split(" ")))
    nextSetup.append(map(int, lines.pop(0).split(" ")))

    print("{} - test".format(case))
    print(firstAnswer)
    print(firstSetup)
    print(nextAnswer)
    print(nextSetup)

    # Take cards in the firstAnswer row
    firstRow = firstSetup[firstAnswer]
    nextRow  = nextSetup[nextAnswer]
    print(firstRow)
    print(nextRow)

    intersection = set(firstRow).intersection(set(nextRow))
    print(intersection)

    l = len(intersection)
    if l == 1:
        output = "Case #{}: {}".format(case, list(intersection)[0])
    elif l == 0:
        output = "Case #{}: Volunteer cheated!".format(case)
    else:
        output = "Case #{}: Bad magician!".format(case)

    print(output)
    a.write(output + "\n")
