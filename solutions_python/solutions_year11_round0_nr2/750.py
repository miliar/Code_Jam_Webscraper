#!/usr/bin/env python2.6

import sys

COMBS = []
OPPS = []
ELES = []
C, D, N = 0, 0, 0

def combine(l):
  if len(l)<2: return l
  a, b = l[-1], l[-2]
  for c in COMBS:
    if c[:2] == a+b or c[:2] == b+a:
      new = l[:len(l)-2]
      new.append(c[-1])
      return new
#      return l[:len(l)-2].append(c[-1])
  return l

def oppose(l):
  if len(l)<2: return l
  newc = l[-1]
  if l.index(newc) != len(l)-1:
    return l
  pairs = []
  for e in l[:len(l)-1]:
    if e <= newc: pairs.append(e+newc)
    else: pairs.append(newc+e)
  pairs = sorted(pairs)
  new_p = []
  for i in range(len(pairs)-1):
    if pairs[i]==pairs[i+1]:
      continue
    else:
      new_p.append(pairs[i])
  new_p.append(pairs[-1])
  for pair in new_p:
    for opp in OPPS:
      if pair==opp:
        return []
  return l
  
T = 0
Ti = 0

for line in sys.stdin:
  if Ti == 0:
    T = int(line.strip())
    Ti = 1
    continue

  l = line.strip().split(' ')
  l.reverse()

  C = int(l.pop())
  for i in range(C):
    COMBS.append(l.pop())

  D = int(l.pop())
  for i in range(D):
    s = l.pop()
    if s[0]<=s[1]: OPPS.append(s)
    else: OPPS.append(s[1]+s[0])
  OPPS = sorted(OPPS)

  N = int(l.pop())
  ELES = [c for c in l.pop()]

  output = []
  for e in ELES:
    output.append(e)
    len_before = len(output)
    output = combine(output)
    if len(output) == len_before-1:
      continue
    else:
      output = oppose(output)

  print 'Case #%d: %s' % (Ti, output.__str__().replace("'",''))
  COMBS = []
  OPPS = []
  ELES = []
  C, D, N = 0, 0, 0

  Ti+=1
  if Ti>T: break
