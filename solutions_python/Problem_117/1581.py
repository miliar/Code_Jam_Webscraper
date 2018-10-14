#!/usr/bin/env python

import sys

def solve(lawn,n,m):
    def can_reach(x,y):
      h = lawn[y][x]
      can = True
      for i in xrange(m):
        if lawn[y][i] > h:
          can = False
          break
      if can:
        return True
        
      for i in xrange(n):
        if lawn[i][x] > h:
          return False
      
      return True


    for j in xrange(n):
      for i in xrange(m):
         if not can_reach(i,j):
           return "NO"
    return "YES"

cases_no = int(sys.stdin.readline())
for case_no in xrange(cases_no):
    [N,M] = map(int,sys.stdin.readline().split())
    lawn = []
    for i in xrange(N):
      lawn.append(map(int,sys.stdin.readline().split()))
  
    res = solve(lawn,N, len(lawn[0]))
    print "Case #%d: %s" % (case_no+1, res)
