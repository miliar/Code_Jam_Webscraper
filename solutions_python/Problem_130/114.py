#!/usr/bin/python

import sys


data = file( sys.argv[1] ).read().splitlines()

l = data.pop( 0 )
NUMCASE = int(l)

def calcmin(N,P):
   teams = 2**N
   for x in xrange(0,teams):
      canbeat = x
      val = 0
      for round in xrange(0,N):
         val = val << 1
         if canbeat:
            canbeat -= 1
            canbeat /= 2
         else:
            val |= 1
      rank = teams - val 
#      print 'rank', x, rank, teams, hex(val)
      if rank > P:
         return x - 1
   return teams - 1

def calcmax(N,P):
   teams = 2**N
   for x in xrange(0,teams):
      t = teams - x - 1
      canbeat = teams- t - 1
      val = 0
      for round in xrange(0,N):
         val = val << 1
         if canbeat:
            val |= 1
            canbeat -= 1
            canbeat /= 2
         else:
            pass
      rank = teams - val 
#      print 'rank', x, rank, teams, hex(val)
      if rank <= P:
         return t
   assert False



for CASE in range(1,NUMCASE+1):
    print 'Case #%d:' % CASE,
    l = data.pop( 0 )
    N, P = [ int(x) for x in  l.split(' ')]
    m = calcmin(N,P)
    v = calcmax(N,P)
    print m, v



