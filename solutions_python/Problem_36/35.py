#!/usr/bin/env python

from sys import stdin

MOD = 10000
target = 'welcome to code jam'

pos = {}
for n in range(26):
   pos[chr(n+ord('a'))] = []
pos[' '] = []

for i in range(len(target)):
   pos[ target[i] ].insert(0, i+1)

TC = int(stdin.readline())
for tc in xrange(TC):
   s = stdin.readline().strip()
   DP = [0] * (len(target)+1)
   DP[0] = 1
   for ch in s:
      if pos.has_key( ch ):
         for k in pos[ ch ]:
            DP[k] += DP[k-1]
            DP[k] %= MOD
   print 'Case #%d: %04d' % (tc+1, DP[-1])
