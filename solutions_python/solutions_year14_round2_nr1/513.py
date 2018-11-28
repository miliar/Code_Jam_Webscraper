#!/usr/bin/env python

import sys

def rl():
  return sys.stdin.readline().strip()

def findmin(numbers):
  ret = 999
  for i in xrange(1, 110):
    x = 0
    for j in xrange(len(numbers)):
      x += abs(i - numbers[j])
    ret = min(x, ret)
  return ret

def solve_one():
  n = int(rl())
  strings = []
  for i in xrange(n):
    strings.append(rl())
  seq = []
  counts = []
  for i in xrange(n):
    prv = ''
    count = [0] * 110
    k = 0
    for j in xrange(len(strings[i])):
      if prv != strings[i][j]:
        if i == 0:
          seq.append(strings[i][j])
        else:
          if k >= len(seq) or seq[k] != strings[i][j]:
            return 'Fegla Won'
        k += 1
        prv = strings[i][j]
      count[k] += 1
    if i != 0 and k != len(seq):
      return 'Fegla Won'
    counts.append(count)
  ret = 0
  for i in xrange(1,k+1):
    numbers = [counts[j][i] for j in xrange(n)]
    ret += findmin(numbers)
  return ret

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
