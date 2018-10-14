#!/usr/bin/env python

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  caseCount = int(fi.readline().strip())
  for i in xrange(1, caseCount+1):
    a, b, k = readInput(fi)
    count = solve(a, b, k)
    displayAndClear(fo, i, count)

def readInput(f):
  a, b, k = [int(arg) for arg in f.readline().split()]
  return a, b, k

def displayAndClear(f, i, count):
  f.write('Case #%d: %d\n' % (i, count))
  f.flush()

def solve(a, b, k):
  count = 0
  for i in range(a):
    for j in range(b):
      if i & j < k:
        count += 1
  return count

if __name__ == '__main__':
  main()

