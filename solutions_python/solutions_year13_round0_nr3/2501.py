#!/usr/bin/env python

import sys
from math import floor, ceil, sqrt

def main():
  f = sys.stdin
  caseCount = int(f.readline().strip())
  for i in range(caseCount):
    lo, hi = [int(arg) for arg in f.readline().split()]
    print 'Case #%i: %i' % (i+1, countFS(lo, hi))

def countFS(lo, hi):
  rlo = int(ceil(sqrt(lo)))
  rhi = int(floor(sqrt(hi)))

  count = 0
  for i in range(rlo, rhi +1):
    if isPalindrome(i):
      n = i**2
      if isPalindrome(n):
        count += 1

  return count

def getDigitList(n):
  digits = []
  base = 10
  while n > 0:
    digits.append(n % base)
    n = n / base
  return digits[::-1]

def isPalindrome(n):
  dList = getDigitList(n)
  for i in range(0, len(dList)/2):
    if dList[i] != dList[-1*(i+1)]:
      return False
  return True

if __name__ == '__main__':
  main()

