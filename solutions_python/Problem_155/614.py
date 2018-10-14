#!/usr/bin/python
__author__ = 'sbuono'

import sys

f = open(sys.argv[1])

nbTestCases = f.readline().strip()

case = 1
for line in f.readlines() :

    line = line.strip()

    ll = line.split()

    maxShyLvl = int(ll[0])

    line = ll[1]


    maxInvite = 0
    spectateurs = 0

    i = 0
    while i <= maxShyLvl :

        friendsNeeded = i - spectateurs

        if friendsNeeded > maxInvite :
            maxInvite = friendsNeeded

        spectateurs += int(line[i])

        i += 1

    print "Case #%d: %d" % (case, maxInvite)

    case += 1