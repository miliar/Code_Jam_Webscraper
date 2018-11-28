#!/usr/bin/python

import sys

lines = []
with open(sys.argv[1], 'r') as FILE:
    lines = FILE.readlines()[1:]

cases = []
for line in lines[1::2]:
    cases.append([int(n) for n in line.split()])

casenumber = 0
for case in cases:
    casenumber += 1

    glist = [i - 1 for i in case]
    slist = list(range(len(glist)))

    hits = 0
    while (glist != slist):
        unheld = {}
        for (cl, el) in enumerate(glist):
            if cl != el:
                unheld[cl] = el
        chain = []
        # Choose one element
        for (cl, el) in unheld.items():
            chain.append(el)
            while (chain[-1] != cl):
                chain.append(unheld[chain[-1]])
            break

        hits += len(chain)
        for l in chain: glist[l] = l

    print("Case #{0}: {1}.000000".format(casenumber, hits))
