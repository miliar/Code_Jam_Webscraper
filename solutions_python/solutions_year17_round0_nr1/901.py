#!/usr/bin/env python
# python 3.6

import queue

def flipped(c):
  if c == '-':
    return '+'
  else:
    return '-'

def search(q, k, init):
  visited = set()
  while not q.empty():
    (steps, s) = q.get()
    if '-' not in s:
      return str(steps)
    if s in visited:
      continue
    visited.add(s)
    for i in range(0, len(s) + 1 - k):
      news = s[0:i] + ''.join([flipped(s[j]) for j in range(i, i+k)]) + s[i+k:]
      q.put((steps+1, news))
  return 'IMPOSSIBLE'

with open('A-small-attempt0.in') as f:
  T = int(f.readline())
  with open('A-small-attempt0.out', 'w') as of:
    for t in range(0,T):
      l = f.readline().strip().split()
      s = l[0]
      k = int(l[1])
      q = queue.Queue()
      q.put((0, s))
      steps = search(q, k, s)
      of.write('Case #' + str(t+1) + ': ' + str(steps) + '\n')
      # print('Case #' + str(t+1) + ': ' + str(steps))
