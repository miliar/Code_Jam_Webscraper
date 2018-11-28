#!/usr/bin/python
import sys

def my_gdc(a, b):
  while b > 0:
    c = a % b
    a = b
    b = c
  return a

def solve(n, pd, pg):
  if pg == 100 and pd != 100:
    return 0
  if pg == 0 and pd != 0:
    return 0
  if pd == 0:
    return 1
  c = my_gdc(100, pd)
  k = 100/c
  if 100/c > n:
    return 0
  # c2 = my_gdc(100, pg)
  # l = 100/c2
  return 1

def main(argv):
  num_tests = int(raw_input())
  for i in xrange(num_tests):
    n, pd, pg = map(int, raw_input().split())
    sol = solve(n, pd, pg)
    if sol == 1:
      print "Case #{0}: Possible".format(i + 1)
    else:
      print "Case #{0}: Broken".format(i + 1)

main(sys.argv)
