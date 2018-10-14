#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, os, sys, random

INBUF = []
OUTBUF = None

def f(x, N):
  return x * N - x * (x - 1) // 2;

def single_test(INBUF, OUTBUF, INDEX):
  P, N = INBUF[INDEX]
  r0, r1 = -1, -1
  
  breakPoints = set([0, 2 ** P - 1])
  bp = 1
  bpm = 2 ** (P - 1)
  while bp < 2 ** P:
    breakPoints.add(bp)
    breakPoints.add(2 ** P - bp)
    bp += bpm
    bpm //= 2
  
  bps = sorted(list(breakPoints))
  
  for j, i in enumerate(bps):
    worst_place = 0
    worst_opponent = 0
    pmod = 2 ** (P - 1)
    omod = 2
    while worst_opponent < i:
      worst_place += pmod
      worst_opponent += omod
      pmod //= 2
      omod *= 2
    
    best_place = 2 ** P - 1
    best_opponent = 2 ** P - 1
    pmod = 2 ** (P - 1)
    omod = 2
    while best_opponent > i:
      best_place -= pmod
      best_opponent -= omod
      pmod //= 2
      omod *= 2
    
    if best_place < N: r1 = bps[j + 1] - 1 if j + 1 < len(bps) else 2 ** P - 1
    if worst_place >= N and r0 == -1: r0 = i - 1
    
    if best_place >= N and r0 != -1: break
  
  if r0 == -1: r0 = 2 ** P - 1
  
  OUTBUF[0][INDEX] = r0
  OUTBUF[1][INDEX] = r1

def fetch_input(IN, INBUF):
  P, N = map(int, IN.readline().split())
  INBUF.append((P, N))


def main(IN, OUT):
  T = int(IN.readline())
  
  OUTBUF = [[None] * T, [None] * T]
  
  for i in range(T):
    fetch_input(IN, INBUF)
  
  for i in range(T):
    single_test(INBUF, OUTBUF, i)
  
  for i in range(T):
    OUT.write('Case #%d: %s %s\n' % (i + 1, str(OUTBUF[0][i]), str(OUTBUF[1][i])))


if __name__ == '__main__':
  assert len(sys.argv) == 2
  IN = open(sys.argv[1], 'rt')
  OUT = open('%s.out' % sys.argv[1][:-3], 'wt')
  main(IN, OUT)
  OUT.close()
  IN.close()

