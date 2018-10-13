#!/usr/bin/python

import sys

def readInput():
  file = open(sys.argv[1])

  testCaseCount = int(file.readline().rstrip())

  testCases = [(int(file.readline()), [int(x) for x in file.readline().rstrip().split()]) for line in xrange(testCaseCount)]
  
  return testCases

def solve((N, numbers)):
  sorted_numbers = sorted(numbers)

  smashes = 0
  for i in xrange(N):
    if numbers[i] != sorted_numbers[i]:
      smashes += 1

  return smashes

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
  print 'Case #%d: %s' % (testCaseNr, solve(testCase))
  testCaseNr += 1
