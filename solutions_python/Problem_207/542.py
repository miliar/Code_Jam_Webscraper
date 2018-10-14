#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def sort2(d, c):
  if len(d) < 2:
    return d
  k = 0
  new_d = []
  while k < (len(d)-1):
    if d[k+1][0] == c and d[k][1] == d[k+1][1]:
      new_d.append(d[k+1])
      new_d.append(d[k])
      k += 2
    else:
      new_d.append(d[k])
      k += 1
  if k == len(d)-1:
    new_d.append(d[k])
  return new_d
      
def solve(t, i):
  n, r, o, y, g, b, v = map(int, t[i].split(' '))
  d = [['R', r], ['O', o], ['Y', y], ['G', g], ['B', b], ['V', v]]
  s = ''
  if r > (y+b) or y > (r+b) or b > (r+y):
    s = 'IMPOSSIBLE'
    print 'Case #%d: %s'%(i+1, s)
    return
  d.sort(key=lambda x:x[1], reverse=True)
  while d != []:
    if s[-1:] == d[0][0]:
      s += d[1][0]
      d[1][1] -= 1
    else:
      s += d[0][0]
      d[0][1] -= 1
    new_d = []
    for a in d:
      if a[1] > 0:
        new_d.append(a)
    d = sorted(new_d, key=lambda x:x[1], reverse=True)
    d = sort2(d, s[0])
  print 'Case #%d: %s'%(i+1, s)

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t, k)
