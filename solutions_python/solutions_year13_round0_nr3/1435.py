#quick and dirty, it's late and I'm heading to bed
from sys import stdin
import math

def readLineIntegers():
  return map(int, stdin.readline().split())

def testPolindrome(n):
  nstr = str(n)
  return nstr == nstr[::-1]

testCases = readLineIntegers()[0]

for test in xrange(testCases):
  low,high = readLineIntegers()
  low, high = int(math.ceil(math.sqrt(low))), int(math.floor(math.sqrt(high)))
  
  count=0
  for n in xrange(low, high+1):
    if testPolindrome(n) and testPolindrome(n*n):
      count += 1
  print 'Case #%d: %d' %(test+1, count)