#!/usr/bin/env python
"""
Solution for Problem A of Qualification Round.

The state of the Snappers behave like bits in binary representation of numbers.
"Snapping" does the same effect to the states as incrementing the number of the
global state by one.

The lamp will be on when all the N Snappers are on, or when the N first bits
are 1. The binary representation for this is reached after 2**N - 1 snaps.
"""

import sys

def isLampOn(N, K):
    mask = (2**N-1)
    return K&mask == mask


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s [inputFile]"%sys.argv[0]
        exit(1)

    inputFileName = sys.argv[1]
    if inputFileName[-3:] == ".in":
        outputFileName = inputFileName[:-3]
    else:
        outputFileName = inputFileName
    outputFileName = outputFileName + ".out"

    inputFile  = open(inputFileName , "r")
    outputFile = open(outputFileName, "w")

    cases = inputFile.readline()
    cases = int(cases.strip())

    for case in xrange(cases):
        line = inputFile.readline().strip()
        args = line.split(" ")
        N = int(args[0])
        K = int(args[1])
        lampOn = isLampOn(N,K)

        if lampOn:
            result = "ON"
        else:
            result = "OFF"

        outputFile.write("Case #%d: %s\n"%(case+1, result))
