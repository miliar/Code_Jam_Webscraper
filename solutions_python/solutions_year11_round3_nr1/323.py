#!/usr/bin/python

import sys

# Read the input file.
f = open(sys.argv[1], "r")
fo = open(sys.argv[1].replace("in", "out"), "w")
lines = f.readlines()
f.close()

testCases = int(lines.pop(0).strip())

i = 0
while i < testCases:
    i += 1

    dimensions = lines.pop(0).strip().split(" ")

    pattern = []

    rows = int(dimensions[0])
    cols = int(dimensions[1])
    amount = rows * cols

    for r in range(int(dimensions[0])):
        row = lines.pop(0).strip()

        pattern.append(row)

    hashFound = False

    for x in range(amount):
        c = x % cols
        r = (x - c) / cols

        if r != rows - 1 and c != cols - 1:
            if pattern[r][c] == "#" and pattern[r][c + 1] == "#" and pattern[r + 1][c] == "#" and pattern[r + 1][c + 1] == "#":
                pattern[r] = pattern[r][:c] + "/\\" + pattern[r][c + 2:]
                pattern[r + 1] = pattern[r + 1][:c] + "\\/" + pattern[r + 1][c + 2:]

        if pattern[r][c] == "#":
            hashFound = True

    fo.write("Case #" + str(i) + ":\n")
    if hashFound:
        fo.write("Impossible\n")
    else:
        for x in range(rows):
            fo.write(pattern[x] + "\n")

