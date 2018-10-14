#!/usr/bin/env python3

import sys

def genPossibleScores():
    regular = dict()
    surprising = dict()
    for i in range(0,31): regular[i] = []; surprising[i] = []
    for a in range(11):
        for b in range(a, 11):
            for c in range(b, 11):
                invalid = abs(a-b) > 2 or abs(a-c) > 2 or abs(b-c) > 2
                if invalid: continue
                isSurprising = abs(a-b) == 2 or abs(a-c) == 2 or abs(b-c) == 2
                if isSurprising: surprising[a+b+c].append( [a, b, c] )
                else:            regular   [a+b+c].append( [a, b, c] )

    return regular, surprising

regular, surprising = genPossibleScores()
def solve(totalPoints, numSurprising, p):
    numGooglers = len(totalPoints)
    c = 0
    for t in totalPoints:
        found = False
        for triplet in regular[t]:
            for s in triplet:
                if s >= p:
                    c += 1
                    found = True
                    break
            if found: break

        if found or numSurprising == 0: continue

        for triplet in surprising[t]:
            for s in triplet:
                if s >= p:
                    c += 1
                    found = True
                    numSurprising -= 1
                    break
            if found: break
    
    return c


# print(regular)
# print("")
# print(surprising)

numcases = int(sys.stdin.readline())
for i in range(numcases):
    line = [int(x) for x in sys.stdin.readline().split()]
    s = line[1]
    p = line[2]
    totalPoints = line[3:]
    print("Case #%d: %d" % (i+1, solve(totalPoints, s, p)))

