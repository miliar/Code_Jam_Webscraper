#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
  f = sys.stdin
  for t in range(int(f.readline())):
    (N, M) = map(lambda x: int(x), f.readline().split(' '))
    dirs = {'/':{}}
    
    # already exists
    for i in range(N):
      cur = dirs
      for item in f.readline().split('/'):
        item = item.strip()
        if len(item) == 0:
          item = '/'
        if not item in cur:
          cur[item] = {}
        cur = cur[item]

    # try to create
    cnt = 0    
    for i in range(M):
      cur = dirs
      for item in f.readline().split('/'):
        item = item.strip()
        if len(item) == 0:
          item = '/'
        if not item in cur:
          cur[item] = {}
          cnt += 1
        cur = cur[item]

    print "Case #%d: %d" % (t+1, cnt)
  

if __name__ == '__main__':
  main()
