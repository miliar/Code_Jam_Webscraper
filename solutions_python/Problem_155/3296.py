#!/usr/bin/python
import sys

def calc(lines):
  have  = 0
  got = 0
  needed = 0
  for i, ins in enumerate(lines):
    if have < i:
      needed += i - have
      have  = i
    have += ins
  return needed

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(1,n+1):
    max_s, ss = d[j].split(" ")
    ss = ss[:-1]
    print "Case #%d: %s" % (j, calc([int(dg) for dg in list(ss)]))

main()
