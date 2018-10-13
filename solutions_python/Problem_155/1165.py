#!/usr/bin/env python

import sys

with file(sys.argv[1]) as inFile:
    testCases = int(inFile.readline())
    for testCase in range(0, testCases):
        smax, humans = inFile.readline().split()

        total = 0
        totalRequired = 0

        for i in range(0, len(humans)):
            level = int(i)
            count = int(humans[i])
            if level > total:
                required = level - total
                totalRequired += required
                total += required
            total += count
        print 'Case #%d: %d' % (testCase + 1, totalRequired)
