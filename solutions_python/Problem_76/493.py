#!/usr/bin/env python

import sys

def main():
  T = int(sys.stdin.readline())
  for test in range(1, T + 1):
    N = int(sys.stdin.readline())
    C = map(int, sys.stdin.readline().split())
    C.sort()

    XOR = reduce(lambda x, y: x ^ y, C)
    SUM = sum(C)
    if XOR == 0:
      print "Case #%d: %d" % (test, SUM - C[0])
    else:
      print "Case #%d: NO" % test
  return 0

if __name__ == "__main__":
  main()

