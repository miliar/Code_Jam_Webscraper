#!/usr/bin/python

import sys
f = open(sys.argv[1], 'r')
f.readline()

case = 0
for l in f.readlines():
  case += 1

  order = []
  t     = {0:[], 1:[]}
  last  = {0:1, 1:1}

  acts = l.split(' ')
  acts.reverse()
  acts.pop()

  while acts:
    curr = (acts.pop() == 'O') and 1 or 0
    order.append(curr)
    prox = int(acts.pop())
    t[curr].extend([1]*abs(prox-last[curr]))
    t[curr].append(0)
    last[curr] = prox

  #print(current)
  #print(t)
  #print(last)

  i = 0
  while order:
    curr = order.pop(0)
    other = curr == 0 and 1 or 0
    i += 1
    if t[other] and t[other][0]:
      t[other].pop(0)
    k = t[curr].pop(0)
    while k:
      i += 1
      if t[other] and t[other][0]:
        t[other].pop(0)
      k = t[curr].pop(0)

  print("Case #{0}: {1}".format(case,i))

