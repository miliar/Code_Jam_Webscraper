#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, os, sys, random
from multiprocessing import Process, BoundedSemaphore, Value, Array

INBUF = []
OUTBUF = None
sem = BoundedSemaphore(8)

def f(x, N):
  return x * N - x * (x - 1) // 2;

def single_test(INBUF, OUTBUF, INDEX):
  sem.acquire()
  result = 0
  N, M, data = INBUF[INDEX]
  
  enter = {}
  leave = {}
  events = set()
  
  cost = 0
  
  for d in data:
    cost += d[2] * f(d[1] - d[0], N)
    cost %= 1000002013
    if d[0] not in events: events.add(d[0])
    if d[0] not in enter: enter[d[0]] = d[2]
    else: enter[d[0]] += d[2]
    if d[1] not in events: events.add(d[1])
    if d[1] not in leave: leave[d[1]] = d[2]
    else: leave[d[1]] += d[2]
    
  
  stack = []
  tricky_cost = 0
  
  for t in sorted(list(events)):
    e = enter[t] if t in enter else 0
    l = leave[t] if t in leave else 0
    stack.append([t, e])
    while l > 0:
      if stack[-1][1] > l:
        tricky_cost += l * f(t - stack[-1][0], N)
        tricky_cost %= 1000002013
        stack[-1][1] -= l
        l = 0
      else:
        tricky_cost += stack[-1][1] * f(t - stack[-1][0], N)
        tricky_cost %= 1000002013
        l -= stack[-1][1]
        stack.pop(-1)
  
  OUTBUF[INDEX] = (1000002013 + cost - tricky_cost) % 1000002013
  sem.release()

def fetch_input(IN, INBUF):
  N, M = map(int, IN.readline().split())
  data = []
  for i in range(M):
    data.append(list(map(int, IN.readline().split())))
  INBUF.append((N, M, data))


def main(IN, OUT):
  T = int(IN.readline())
  
  OUTBUF = Array('i', T)
  
  for i in range(T):
    fetch_input(IN, INBUF)
  
  processes = []
  
  for i in range(T):
    p = Process(target=single_test, args=(INBUF, OUTBUF, i))
    p.start()
    processes.append(p)
  
  for i in range(T):
    processes[i].join()
  
  for i in range(T):
    OUT.write('Case #%d: %s\n' % (i + 1, str(OUTBUF[i])))


if __name__ == '__main__':
  assert len(sys.argv) == 2
  IN = open(sys.argv[1], 'rt')
  OUT = open('%s.out' % sys.argv[1][:-3], 'wt')
  main(IN, OUT)
  OUT.close()
  IN.close()

