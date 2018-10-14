#!/usr/bin/env python

import sys

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print 'need input file'
    exit(0)

  f = open(sys.argv[1])
  cases_no = int(f.readline())
  for i in xrange(cases_no):
    numbers = list(map(int, f.readline()[:-1].split(' ')))

    N = numbers[0]
    S = numbers[1]
    p = numbers[2]
    points = numbers[3:]

    non_surprising = 0
    surprising = 0

    for j in xrange(N):
      if points[j] >= 3 * p - 2:
        non_surprising += 1
      elif points[j] >= 3 * p - 4 and surprising < S:
        if p >= 2:
          surprising += 1 
    print 'Case #%d: %d' % (i + 1, non_surprising + surprising)
