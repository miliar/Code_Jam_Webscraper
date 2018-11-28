#!/usr/bin/python
from sys import stdin

def chick_dist(c, b):
  return b - int(c)

def zip_chick(i, d, s):
  bump = 0
  if (d / s) * s < d:
    bump = 1
  return [i, d / s + bump]
  
def optimize_chicks(chicks, k, t):
  # Walk backwards across the list of chicks.
  chicks = chicks[::-1]
  chicks = filter(lambda c: c[1] <= t, chicks)
  l = len(chicks)

  if k == 0:
    return 0
 
  if l < k:
    return None
  
  swaps = chicks[0][0]
  chicks[0][0] = 0
  for i in xrange(1, k):
    swaps += chicks[i][0] - chicks[i-1][0] - 1
    chicks[i][0] = chicks[i-1][0] + 1
  
  return swaps

cases = int(stdin.readline())

for _ in xrange(cases):
  n, finish, barn, time = map(int, stdin.readline().split(' '))
  distances = map(lambda c: chick_dist(c, barn), stdin.readline().split(' '))
  speeds    = map(int, stdin.readline().split(' '))
  chicks    = [zip_chick(n - i - 1, distances[i], speeds[i]) for i in xrange(n)]
  
  swaps = optimize_chicks(chicks, finish, time)
  if swaps == None:
    print "Case #" + str(_ + 1) + ": IMPOSSIBLE"
  else:
    print "Case #" + str(_ + 1) + ": " + str(swaps)
