#!/usr/bin/env python

import sys

def gcd(a, b):
  while a:
      a, b = b%a, a
  return b

def abs(x):
  if x<0:
    return -1*x
  return x

def gcd_list(lst):
  cur_gcd = lst[0]
  if len(lst) == 1:
    return cur_gcd
  for i in xrange(1,len(lst)):
    cur_gcd = gcd(cur_gcd, lst[i])
  return cur_gcd


def main():
  c = int(sys.stdin.readline().strip())
  line_count = 1
  for line in sys.stdin:
    split_line = line.split()
    ges = []
    for i in xrange(1, len(split_line)):
      ges.append(int(split_line[i]))
    diffs = []
    for i in xrange(0, len(ges)):
      for j in xrange(i, len(ges)):
        diffs.append(abs(ges[i]-ges[j]))
    ges_gcd = gcd_list(ges)
    diffs_gcd = gcd_list(diffs)
    if diffs_gcd == 1:
      print "Case #%s: %d" % (line_count, 0)
    else:
      next_t = diffs_gcd - (ges[0] % diffs_gcd)
      if next_t == diffs_gcd:
        next_t = 0
      print "Case #%s: %d" % (line_count, next_t)

    line_count += 1



if __name__ == "__main__":
  main()
