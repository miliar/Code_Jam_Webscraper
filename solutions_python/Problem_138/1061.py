#!/usr/bin/python
import os, sys, math, bisect

def solve(naomiBlocks, kenBlocks):
    warPoints = 0
    deceitfulWarPoints = 0
    # lowest blocks first
    nBs = sorted(naomiBlocks)
    kBs = sorted(kenBlocks)
    # Regular war
    for i in range(len(nBs)):
        nB = nBs[0]
        del nBs[0]
        if (nB > kBs[len(kBs)-1]):
            # naomi has to win, ken chooses worst one
            del kBs[0]
            warPoints += 1
        else:
            # ken chooses the least one that is greater than naomi's
            pos = bisect.bisect_left(kBs, nB)
            assert kBs[pos] > nB
            del kBs[pos]

    # lowest blocks first
    nBs = sorted(naomiBlocks)
    kBs = sorted(kenBlocks)
    # Deceitful war
    # strategy: 
    # 1) if she can, pick her lowest and say really high (only works if her lowest > ken's lowest)
    # 2) if not, if she can, pick her lowest and say a tiny bit less than
    # ken's highest
    for i in range(len(nBs)):
        if (nBs[0] > kBs[0]):
            # go naomi! (1)
            nB = 1.0
            del nBs[0]
        elif (nBs[0] < kBs[len(kBs)-1]):
            # go naomi! (2)
            nB = kBs[len(kBs)-1] - 0.000001
            del nBs[0]
        else:
            nB = nBs[0]
            del nBs[0]
        if (nB > kBs[len(kBs)-1]):
            # naomi has to win, ken chooses worst one
            del kBs[0]
            deceitfulWarPoints += 1
        else:
            # ken chooses the least one that is greater than naomi's
            pos = bisect.bisect_left(kBs, nB)
            assert kBs[pos] > nB
            del kBs[pos]

    return [deceitfulWarPoints, warPoints]


def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        numBlocks = int(fileLines[index][:-1])
        index += 1
        naomiBlocks = [float(x) for x in fileLines[index][:-1].split()]
        index += 1
        kenBlocks = [float(x) for x in fileLines[index][:-1].split()]
        index += 1
        answer = solve(naomiBlocks, kenBlocks)
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, ' '.join([str(x) for x in answer]))

if __name__ == '__main__':
    main(sys.argv[1])
