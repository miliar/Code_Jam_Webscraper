#!/bin/env python

import sys
import re

def testcase(fileName):
    L = None
    D = None
    N = None
    wordList = []
    testCase = 0
    for line in open(fileName):
        if L is None:
            L = int(line.split()[0])
            D = int(line.split()[1])
            N = int(line.split()[2])
            continue
        if D:
            D -= 1
            wordList.append(line)
            continue
        if testCase < N:
            testCase += 1
            regExp = line.replace('(', '[').replace(')', ']')
            prog = re.compile(regExp)
            count = 0
            for word in wordList:
                if prog.match(word): count += 1
            print "Case #" + str(testCase) + ": " + str(count)

if __name__ == '__main__':
    testcase(sys.argv[1])

