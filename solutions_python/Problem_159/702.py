#!/usr/bin/env python

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  caseCount = int(fi.readline().strip())
  for i in range(1, caseCount+1):
    counts = readInput(fi)
    e1, e2 = solve(counts)
    displayAndClear(fo, i, e1, e2)

def readInput(f):
  f.readline()
  counts = [int(arg) for arg in f.readline().split()]
  return counts

def displayAndClear(f, i, e1, e2):
  f.write('Case #%d: %d %d\n' % (i, e1, e2))
  f.flush()

def solve(counts):
  n = len(counts)
  eats1 = solve1(counts, n)
  eats2 = solve2(counts, n)
  return eats1, eats2

def solve1(counts, n):
  eats = 0
  prev = counts[0]
  for i in xrange(1, n):
    diff = prev - counts[i]
    if diff > 0:
      eats += diff
    prev = counts[i]
  return eats

def solve2(counts, n):
  maxStep = -1*float('inf')
  prev = counts[0]
  for i in xrange(1, n):
    diff = prev - counts[i]
    maxStep = max(maxStep, diff)
    prev = counts[i]

  eats = 0
  for i in xrange(0, n-1):
    cur = counts[i]
    eats += min(cur, maxStep)
  return eats

if __name__ == '__main__':
  main()

