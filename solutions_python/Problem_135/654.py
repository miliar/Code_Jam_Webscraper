#!/usr/bin/env python
import sys

def solve():
  row1 = int(sys.stdin.readline())
  for n in xrange(1, 5):
    line = sys.stdin.readline()
    if n == row1:
      rowset1 = set(map(int, line.split(' ')))

  row2 = int(sys.stdin.readline())
  for n in xrange(1, 5):
    line = sys.stdin.readline()
    if n == row2:
      rowset2 = set(map(int, line.split(' ')))

  intersect = rowset1 & rowset2
  l = len(intersect)
  if l == 0:
    return 'Volunteer cheated!'
  if l == 1:
    return str(intersect.pop())
  return 'Bad magician!'

tests = int(sys.stdin.readline())
for case in xrange(1, tests + 1):
  result = solve()
  print "Case #%d: %s" % (case, result)
