#!/usr/bin/env python
# encoding: utf-8

import sys
import math

inFileName = sys.argv[1]
outFileName = sys.argv[2]


def calc(nrs):
    return "%d %d" % (m1(nrs), m2(nrs))


def m1(nrs):
    prev = 0
    sumi = 0
    for nr in nrs:
        if prev > nr:
            sumi += prev - nr
        prev = nr
    return sumi


def m2(nrs):
    eaten = 0
    prev = 0
    rate = 0
    for nr in nrs:
        rate = max(max(prev - nr, 0), rate)
        prev = nr
    print("rate %d" % rate)
    for nr in nrs[:-1]:
        eat = 0
        if nr >= rate:
            eat += rate
        else:
            eat += nr
        eaten += eat
        print(eat)
    return eaten

with open(inFileName, "r") as inFile, open(outFileName, "w") as out:
    header = inFile.readline()
    nrCases = int(header)
    lines = inFile.readlines()
    for i, (line1, line2) in enumerate(zip(lines[::2], lines[1::2])):
        if i >= nrCases:
            print("overflow")
            break
        nrs = list(map(int, line2.strip().split(" ")))
        if len(nrs) != int(line1):
            print("invalid data")
        lsg = calc(nrs)
        print("Case #%d: %s" % (i + 1, lsg))
        print("Case #%d: %s" % (i + 1, lsg), file=out)
