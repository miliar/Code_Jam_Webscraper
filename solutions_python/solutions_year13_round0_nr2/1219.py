#!/usr/bin/python
import sys

def lane_doable(lane, height):
  return max(lane) <= height

def lanes(lawn, n, m):
  result = []
  for row in range(n):
    result.append([lawn[i] for i in range(row*m, row*m+m)])
  for col in range(m):
    result.append([lawn[i] for i in range(col, col+n*m, m)])
  return result

def lanes_of_square(lawn, n, m, i, j):
  return [[lawn[k] for k in range(i*m, i*m+m)]] + [[lawn[k] for k in range(j, j+n*m, m)]]

def doable(lawn, n, m):
  for i in range(n):
    for j in range(m):
      lanes = lanes_of_square(lawn, n, m, i, j)
      if [lane_doable(lane, lawn[i*m+j]) for lane in lanes].count(True) == 0:
        return False
  return True

if __name__ == '__main__':
  n_cases = int(raw_input())
  for case in range(1, n_cases+1):
    (n,m) = [int(s) for s in raw_input().split()]
    lawn = []
    for row in range(n):
      lawn.extend([int(s) for s in raw_input().split()])
    if doable(lawn, n, m):
      print "Case #%d: YES" % case
    else:
      print "Case #%d: NO" % case

