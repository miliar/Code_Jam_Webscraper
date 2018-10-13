#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
  T = int(sys.stdin.readline())
  for i in range(T):
    euro = 0
    (R, K, N) = map(lambda x: long(x), sys.stdin.readline().split(' '))
    groups = map(lambda x: long(x), sys.stdin.readline().split(' '))
    for j in range(R):
      # ride on coaster
      cur = []
      while True:
        if sum(cur) + groups[0] <= K:
          cur.append(groups.pop(0))
        else:
          break
        if len(groups) == 0:
          break
      # run coaster
      euro += sum(cur)
      groups.extend(cur)
    print "Case #%d: %d" % (i+1, euro)

if __name__ == '__main__':
  main()
