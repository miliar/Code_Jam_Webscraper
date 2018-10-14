#!/usr/bin/python

import sys

def line():
    return sys.stdin.readline()[:-1]

if __name__ == '__main__':
    numberOfCases = int(line())
    for caseNumber in range(numberOfCases):
        case = line().split()
        C = int(case[0])
        combinations = case[1:C+1]
        D = int(case[C+1])
        oppositions = case[C+2:C+D+2]
        N = int(case[C+D+2])
        invocations = case[C+D+3]

        changingPairs = dict()
        for triplet in combinations:
            changingPairs[tuple(triplet[:2])] = triplet[-1]
            changingPairs[(triplet[1],triplet[0])] = triplet[-1]
            
        enemies = dict()
        for a, b in oppositions:
            if a not in enemies:
                enemies[a] = set()
            if b not in enemies:
                enemies[b] = set()
            enemies[a].add(b)
            enemies[b].add(a)

        possessions = list()
        for base in invocations:
            if len(possessions) > 0 and (base,possessions[-1]) in changingPairs:
                removedElement = possessions.pop(-1)
                possessions.append(changingPairs[(base,removedElement)])
            elif base in enemies and (not set(possessions).isdisjoint(enemies[base])):
                possessions = list()
            else:
                possessions.append(base)
        print "Case #" + str(caseNumber+1) + ": " + str(possessions).replace("'",'')
