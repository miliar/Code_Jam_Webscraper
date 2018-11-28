#!/usr/bin/env python

import sys

def show(arr):
    return '[' + ', '.join(arr) + ']'

def testOpp(current, c, oppositions):
    for o in current:
        if c+o in oppositions or o+c in oppositions:
            return True
    return False

def runtest(inf, testno):
    transitions = dict()
    oppositions = set()
    current = []
    line = inf.readline().split()
    # Read transitions
    C = int(line[0])
    for i in xrange(1,C+1):
        trans = line[i]
        transitions[trans[0:2]] = trans[2]
    # Read oppositions
    D = int(line[C+1])
    for i in xrange(C+2, C+D+2):
        oppositions.add(line[i])
    # Run through characters
    characters = line[-1]
    for c in characters:
        if len(current) == 0:
            current.append(c)
        else:
            o = current[-1]
            if c+o in transitions:
                current[-1] = transitions[c+o]
            elif o+c in transitions:
                current[-1] = transitions[o+c]
            elif testOpp(current, c, oppositions):
                current = []
            else:
                current.append(c)

    print 'Case #' + str(testno+1) + ': ' + show(current)

inf = open(sys.argv[1], 'r')
numtests = int(inf.readline().strip())
for i in xrange(numtests):
    runtest(inf, i)
inf.close()
