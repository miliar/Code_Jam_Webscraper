#!/usr/bin/env python

import sys

f = open('A-small-attempt1.in')

cards1 = []
cards2 = []

row1 = None
row2 = None

T = int(f.readline())

for i in range(1, T+1):
    cards1 = []
    cards2 = []
    row1 = int(f.readline())
    for j in range(0,4):
        cards1.append(f.readline().split())
    row2 = int(f.readline())
    for j in range(0,4):
        cards2.append(f.readline().split())
    possible = [x for x in cards1[row1-1] if x in cards2[row2-1]]
    if len(possible) == 1:
        print "Case #{0}: {1}".format(i, possible[0])
    elif len(possible) == 0:
        print "Case #{0}: Volunteer cheated!".format(i)
    else:
        print "Case #{0}: Bad magician!".format(i)
