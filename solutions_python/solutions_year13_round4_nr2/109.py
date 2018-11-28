#!/usr/bin/python2
#-*- coding: utf-8 -*-

import math

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def can_win(N, n):
  return int(math.log(2**N - n, 2))

def can_lose(N, n):
  return int(math.log(n+1, 2))

for test in range(readint()):
  print 'Case #%i:'%(test+1),
  N, P = readarray(int)

  if P == 2**N:
    print 2**N-1, 2**N-1
    continue

  max_ones_low = int(math.log(P, 2))
  min_ones_high = N - int(math.log(2**N - P, 2))

  goal_lose = min_ones_high
  goal_win = N - max_ones_low

  guaranteed = 2**goal_lose - 2 if goal_lose > 0 else 0
  could = 2**N - (2**goal_win if goal_win > 0 else 0)

  print guaranteed, could
