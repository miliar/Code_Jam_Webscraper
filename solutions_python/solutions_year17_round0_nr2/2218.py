#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def readint(): return int(input())
def readfloat(): return float(input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, input().split())

def tidy(n):
  original = list(str(n))
  sorted_list = sorted(list(str(n)))
  return original == sorted_list

def solve(n):
  while not tidy(n):
    n -= 1
  return n

def solve_smart(n):
  if tidy(n): return n

  ln = list(map(int, list(str(n))))
  
  # find biggest number before number is not tidy anymore
  biggest_number = None
  last_seen = None
  for i in range(len(ln)):
    current = ln[i]
    if last_seen is None:
      last_seen = current
      continue
      
    if current < last_seen:
      biggest_number = last_seen
      break
      
    last_seen = current
  
  # create last tidy number
  broken_yet = False
  ans = ''
  for i in range(len(ln)):
    current = ln[i]
    if broken_yet:
      ans += '9'
    elif current == biggest_number:
      ans += str(current - 1)
      broken_yet = True
    else:
      ans += str(current)
  
  ans = ans.lstrip('0')
  
  ans = int(ans)
  
  return ans
  
if __name__ == '__main__':

  # '0000012345'.lstrip('0')

  #for i in range(10000):
  #  ss = solve(i)
  #  sss = solve_smart(i)
  #  #if i != ss:
  #  #  print(str(i) + ' ' + str(ss))
  #  if ss != sss:
  #    print(str(i) + ': <' + str(ss) + '> <' + str(sss) + '>')
  #
  #sys.exit(0)

  T = readint()
  for t in range(1, T+1):
    n = int(input())
    ans = solve_smart(n)
    print('Case #%d: %s' % (t, ans))