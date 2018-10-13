#!/usr/bin/env python

import sys

def get_min(amote, bigger_motes):
    if len(bigger_motes) == 0:
        return 0

    if amote > bigger_motes[0]:
        # Eat the next one
        amote = amote + bigger_motes[0]
        return get_min(amote, bigger_motes[1:])
    else:
        # Add one
        if amote > 1:
            a = 1 + get_min(amote * 2 - 1, bigger_motes)
        else:
            a = sys.maxint
        # Remove one
        b = 1 + get_min(amote, bigger_motes[1:])
        return min(a, b)

fin = open(sys.argv[1])
fin.readline()
lines = fin.readlines()

for i in range(0, len(lines) / 2):
    amote = lines[i * 2].strip().split()
    amote = amote[0]
    amote = int(amote)

    motes = lines[i * 2 + 1].strip().split()
    motes = [int(x) for x in motes]

    motes = sorted(motes)
    bigger_motes = []
    for m in motes:
        if m < amote:
            amote += m
        else:
            bigger_motes.append(m)
    print "Case #%d: %d" % (i+1, get_min(amote, bigger_motes))
    



