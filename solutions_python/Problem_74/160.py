#!/usr/bin/env python

from sys import stdin

class State:
   def __init__(self, _pos = 1, _time = 0):
      self.pos  = _pos
      self.time = _time

TC = int(stdin.readline().strip())
for tc in xrange(1, TC+1):
   A = stdin.readline().split()
#  N = int(A[0])
   states = [ State(), State() ]
   t = 0
   for i in xrange(1, len(A), 2):
      k = 0 if A[i] == 'B' else 1
      pos = int(A[i+1])
      states[k].time = max(t, states[k].time + abs(pos - states[k].pos)) + 1
      states[k].pos = pos
      t = states[k].time
   res = max(states[0].time, states[1].time)
   print 'Case #%d: %d' % (tc, res)
