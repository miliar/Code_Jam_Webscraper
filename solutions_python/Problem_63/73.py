#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

def main():
  tree_nodes = []
  tmp = 1
  cur = 1
  while tmp <= 10 ** 9:
    tree_nodes.append(tmp)
    tmp += 2**cur
    cur += 1
  
  f = sys.stdin
  for t in range(int(f.readline())):
    (L, P, C) = map(int, f.readline().strip().split(' '))

    x = 0
    LL = L
    while True:
      LL = LL * C
      if LL >= P:
        break
      x += 1

    cnt = 0
    if x > 0:
      for node in tree_nodes:
        cnt += 1        
        if x <= node:
          break
    print 'Case #%d: %d' % (t+1, cnt)

if __name__ == '__main__':
  main()
