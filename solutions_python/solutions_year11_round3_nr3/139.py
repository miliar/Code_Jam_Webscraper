#!/usr/bin/python

import sys

EXAMPLE = 0

def solve(L, H, case):
    i = L
    while i <= H:
        ok = 1
        for note in case:
            if note == 1:
                pass
            elif note % i == 0 or i % note == 0:
                pass
            else:
                ok = 0
                break
        if ok == 1:
            return i
        i += 1
    return "NO"

def main(data = "C-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    T = int(inp[0])
    i = 1
    j = 0
    while j < T:
        j += 1
        print "Case #" + str(j) + ":",
        N, L, H = map(int, inp[i].split())
        i += 1
        print solve(L, H, map(int, inp[i].split()))
        i += 1


if EXAMPLE:
    main()
else:
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print sys.argv[0] + " <input file>"
