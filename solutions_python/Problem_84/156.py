#!/usr/bin/python

import sys

EXAMPLE = 0

def solve(R, C, case):
    x = 0
    while x < R:
        y = 0
        while y < C:
            if case[x][y] == "#":
                if y + 1 == C or x + 1 == R:
                    return "Impossible"
                if case[x][y+1] != "#" or case[x+1][y] != "#" or case[x+1][y+1] != "#":
                    return "Impossible"
                case[x] = case[x][:y] + "/\\" + case[x][y+2:]
                case[x+1] = case[x+1][:y] + "\\/" + case[x+1][y+2:]
            y += 1
        x += 1
    return "\n".join(case)

def main(data = "A-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    T = int(inp[0])
    i = 1
    j = 0
    while j < T:
        j += 1
        print "Case #" + str(j) + ":"
        R, C = map(int, inp[i].split())
        i += 1
        print solve(R, C, inp[i:i+R])
        i += R


if EXAMPLE:
    main()
else:
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print sys.argv[0] + " <input file>"
