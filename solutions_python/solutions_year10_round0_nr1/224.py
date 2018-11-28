#!/usr/bin/python

import sys
import os.path

if len(sys.argv) < 2:
    print('snapper.py file')
    exit(0)

infile = sys.argv[1]
try:
    input = open(infile, 'r')
except:
    print('error opening the file')
    exit(0)
nbTestCaseTxt = input.readline()
try:
    nbTestCase = int(nbTestCaseTxt)
except:
    print('incorrect format for the number of test case')
    exit(0)
testCasesTxt = list()
try:
    for i in range(nbTestCase):
        line = input.readline()
        testCasesTxt.append(line)
except:
    print('wrong number of test cases')
    exit(0)
testCases = list()
for s in testCasesTxt:
    try:
        (nTxt, kTxt) = s.split()
        n = int(nTxt)
        k = int(kTxt)
        testCases.append({ 'n':n, 'k':k })
    except:
        print('incorrect format for a test case')
        exit(0)
for i in range(len(testCases)):
    testCase = testCases[i]
    n = testCase.get('n')
    k = testCase.get('k')
    p = 2 ** n
    if k % p == p - 1:
        print('Case #%d: ON' % (i + 1))
    else:
        print('Case #%d: OFF' % (i + 1))
