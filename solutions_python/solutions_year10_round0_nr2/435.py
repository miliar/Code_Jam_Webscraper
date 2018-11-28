#!/usr/bin/python

import sys
import os.path

if sys.version_info < (2,6):
    raise "You need python 2.6 to run this program"

import fractions

if len(sys.argv) < 2:
    print('fairWarning.py file')
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
        line = s.split()
        n = int(line[0])
        if n <= 0 or n != len(line[1:]):
            raise 
        testCase = list()
        for s in line[1:]:
            testCase.append(int(s))
        testCases.append(testCase)
    except:
        print('incorrect format for a test case')
        exit(0)
for i in range(len(testCases)):
    testCase = testCases[i]
    n = len(testCase)
    minimum = min(testCase)
    if n == 1:
        t = testCase[0]
    elif n == 2:
        t = abs(testCase[0] - testCase[1])
    else:
        t = fractions.gcd(abs(testCase[0] - testCase[1]), abs(testCase[1] - testCase[2]))
        for j in range(2, len(testCase) - 1):
            a = abs(testCase[j] - testCase[j + 1])
            t = fractions.gcd(t, a)
    k = minimum / t
    while t * k - minimum < 0:
        k = k + 1
    print('Case #%d: %d' % (i + 1, t * k - minimum))
