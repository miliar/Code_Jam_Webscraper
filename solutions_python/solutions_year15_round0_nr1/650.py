#!/usr/bin/env python

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  caseCount = int(fi.readline().strip())
  for i in range(1, caseCount+1):
    ss = readInput(fi)
    solution = solve(ss)
    displayAndClear(fo, i, solution)

def readInput(f):
  args = f.readline().split()[1]
  ss = [int(ch) for ch in args]
  return ss

def displayAndClear(f, i, solution):
  f.write('Case #%d: %d\n' % (i, solution))
  f.flush()

def solve(ss):
  missing = 0
  total = 0
  for sLevel, sCount in enumerate(ss):
    curMissing = 0
    if sLevel > total:
      curMissing = sLevel - total
    missing += curMissing
    total +=  curMissing + sCount
  return missing

if __name__ == '__main__':
  main()

