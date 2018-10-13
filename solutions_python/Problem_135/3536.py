#!/usr/bin/env python
import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
  arr_first = []
  arr_second = []

  first = int(rl())
  arr_first.append(set(map(int, rl().split())))
  arr_first.append(set(map(int, rl().split())))
  arr_first.append(set(map(int, rl().split())))
  arr_first.append(set(map(int, rl().split())))

  second  = int(rl())
  arr_second.append(set(map(int, rl().split())))
  arr_second.append(set(map(int, rl().split())))
  arr_second.append(set(map(int, rl().split())))
  arr_second.append(set(map(int, rl().split())))

  ans = list(arr_first[first-1] & arr_second[second-1])
  if len(ans) == 1:
    print 'Case #%d: %d' % (i+1,ans[0])
  elif len(ans) > 1:
    print 'Case #%d: Bad magician!' % (i+1)
  elif len(ans) == 0:
    print 'Case #%d: Volunteer cheated!' % (i+1)


