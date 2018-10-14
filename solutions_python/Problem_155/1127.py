#!/usr/bin/env python

import fileinput

def findMinimumInvites(testcase):
   invites = 0

   for i in xrange(len(testcase)-1, -1, -1):
      if testcase[i] > 0:
         if invites == 0:
            invites = i
         else:
            invites = max(invites - testcase[i], i)

   return invites

if __name__ == "__main__":
   lineCount = 0
   testcaseCount = 0
   testcases = []

   for line in fileinput.input():
      if lineCount == 0:
         testcases = long(line) * [None]
         lineCount += 1
      else:
         tokens = line.split()
         size = long(tokens[0]) + 1
         shynesses = size*[None]
         for i in xrange(size):
            shynesses[i] = long(tokens[1][i])
         testcases[testcaseCount] = shynesses
         testcaseCount += 1
         lineCount += 1

   testcaseCount = 0

   for testcase in testcases:
      testcaseCount += 1
      print ("Case #%ld: %ld" % (testcaseCount, findMinimumInvites(testcase)))
