#!/usr/bin/env python

from __future__ import print_function, division

import math
import os
import os.path
import sys


def main():
    inFile = open(sys.argv[1], "rt")
    outFile = open(sys.argv[2], "wt")

    numCases = int(inFile.readline())

    for caseNum in xrange(1, numCases+1):
        print("*** Case {0:d} ***".format(caseNum))

        args = inFile.readline().split()
        numActs, numSuprises, threshold = (int(s) for s in args[0:3])
        actTotals = [int(s) for s in args[3:]]
        assert len(actTotals) == numActs

        aboveThreshold = 0
        suprisesLeft = numSuprises

        for actTotal in actTotals:
            regMin = actTotal // 3

            if actTotal % 3 == 0:
                regMax = regMin
            else:
                regMax = regMin + 1

            supMin = regMin - 1
            supMax = regMax + 1

            print(regMin, regMax, supMin, supMax)

            if regMax >= threshold:
                aboveThreshold += 1
                continue

            # test for suprise use
            if suprisesLeft == 0:
                continue

            if actTotal % 3 == 1:
                continue    # cannot diff by > 2

            if supMin < 0 or supMax > 10:
                continue

            # use suprise
            if supMax >= threshold:
                aboveThreshold += 1
                suprisesLeft -= 1

        print("suprises used: ", numSuprises - suprisesLeft)
        outFile.write("Case #{0:d}: {1:d}\n".format(caseNum, aboveThreshold))

    inFile.close()
    outFile.close()


if __name__ == "__main__": main()
