#!/usr/bin/env python

import sys
import bisect

case_num = 1

def solve_deceitful(naomi, ken):
  n = naomi[:]
  n.reverse()
  k = ken[:]
  add = 0
  while len(n) >= 1 and n[-1] < k[-1]:
    if n[-1] > k[0]:
      n.pop()
      k.pop(0)
      add += 1
    else:
      n.pop()
      k.pop()
  n.sort()
  return len(k) + add

def solve_truth(naomi, ken):
  k = ken[:]
  for x in naomi:
    pos = bisect.bisect(k, x)
    if (pos == len(k)):
      break
    else:
      k.pop(pos)
  return len(k)

with open(sys.argv[1],'r') as f:
  num_testcases = int(f.readline())
  for i in xrange(num_testcases):
    num_blocks = f.readline()
    naomi = map(float, f.readline().strip().split())
    naomi.sort()
    ken = map(float, f.readline().strip().split())
    ken.sort()
    y = solve_deceitful(naomi, ken)
    z = solve_truth(naomi, ken)
    print "Case #%d: %d %d" % (case_num, y, z)
    case_num += 1
