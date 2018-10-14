#!/usr/bin/python

import sys
from collections import defaultdict

def getNumMoves(ss):
   maxlen = max([len(s) for s in ss])
   offsets = [ 0 for s in ss]

   moves = 0

   prev = ''
   while prev != ' ':
      vals = defaultdict(int)
      for s,offset in zip(ss,offsets):
         #count types
         vals[s[offset]] += 1
      if len(vals.keys()) > 2:
         return -1
      
      if len(vals.keys()) < 2:
         for sidx in range(0,len(ss)):
            offsets[sidx] += 1
         prev, = vals.keys()
         #print "Matched: " + prev
         continue

      k1,k2 = vals.keys()
      
      if vals[k1] > vals[k2] or (vals[k1] == vals[k2] and k1 == prev):
         ka = k1
         kb = k2
      else:
         kb = k1
         ka = k2
      
      if ka == prev:
         #should add letter
         for sidx in range(0,len(ss)):
            if ss[sidx][offsets[sidx]] == ka:
               offsets[sidx] += 1
            else:
               moves += 1
               #print "Add " + ka + " to " + str(sidx)
      elif kb == prev:
         #should delete letter
         for sidx in range(0,len(ss)):
            if ss[sidx][offsets[sidx]] == kb:
               offsets[sidx] += 1
               moves += 1
               #print "Remove " + kb + " from " + str(sidx)
      else:
         #can't do anything
         return -1
      prev = ka
   return moves

def processCase(case):
   N = int(sys.stdin.readline())
   ss = []
   for n in range(0,N):
      ss.append(sys.stdin.readline().strip()+"  ")
   
   moves = getNumMoves(ss)
   
   if moves >= 0:
      print "Case #%d: %d" % (case+1,moves)
   else:
      print "Case #%d: Fegla Won" % (case+1,)

num = int(sys.stdin.readline())

for case in range(0,num):
    processCase(case)
