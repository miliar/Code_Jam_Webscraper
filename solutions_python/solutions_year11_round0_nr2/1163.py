#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print("No input file specified.")
    sys.exit(0)

infilename = sys.argv[1]
infile = open(infilename, "r")
ncases = int(infile.readline())

for i in range(ncases):
    ln = infile.readline().split()
    c = int(ln[0])
    d = int(ln[1+c])
    n = int(ln[2+c+d])
    elements = []
    combines = {}
    opposes = []

    for j in range(c):
        tmp = ln[1+j]
        combines[tmp[:2]] = tmp[-1]

    for j in range(d):
        opposes.append(ln[2+c+j])

    for j in range(n):
        elem = ln[-1][j]

        if len(elements) > 0:
            for com in combines:
                val = combines[com]
                if (com[0] == elements[-1] and com[1] == elem) or (com[0] == elem and com[1] == elements[-1]):
                    elements.pop()
                    elem = val
                    break

        elements.append(elem)
        for opp in opposes:
            if opp[0] in elements and opp[1] in elements:
                elements = []

    out = "Case #%d: %r" % (i + 1, elements)
    print(out.replace("'", ''))
