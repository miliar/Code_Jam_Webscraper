#!/usr/bin/python

import sys

def readInput():
  file = open(sys.argv[1])

  testCaseCount = int(file.readline().rstrip())

  testCases = [(int(file.readline()), [int(x) for x in file.readline().rstrip().split()]) for line in xrange(testCaseCount)]
  
  return testCases

def patricksum(numbers):
  return reduce(lambda x,y: x^y, numbers)

def solve((N, numbers)):
  if patricksum(numbers) != 0:
    return 'NO'

  return sum(numbers) - min(numbers)

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
  print 'Case #%d: %s' % (testCaseNr, solve(testCase))
  testCaseNr += 1
