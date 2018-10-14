#!/usr/bin/env python
# encoding: utf-8

import sys

inFileName = sys.argv[1]
outFileName = sys.argv[2]


def calc(sMax, audience):
    # convert to arr
    audience = list(map(int, list(audience)))
    if len(audience) != sMax + 1:
        print("invalid numbers", len(audience), sMax)
        return -1
    addedFriends = 0
    currAudience = 0
    for i in range(sMax + 1):
        if currAudience < i:
            # we need to add friends
            newFriends = i - currAudience
            addedFriends += newFriends
            currAudience += newFriends
            #print("added friends at %d" % i)
        currAudience += audience[i]
        #print("audience: %d, i: %d" % (currAudience, i))

    return addedFriends

with open(inFileName, "r") as inFile, open(outFileName, "w") as out:
    header = inFile.readline()
    nrCases = int(header)
    for i, line in enumerate(inFile):
        if i >= nrCases:
            break
        cells = line.strip().split(" ")
        lsg = calc(int(cells[0]), cells[1])
        print("Case #%d: %d" % (i + 1, lsg), file=out)
