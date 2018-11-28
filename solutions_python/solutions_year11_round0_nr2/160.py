#!/usr/bin/env python

def check_opposed(elements, ele, dic):
  for e in elements:
    if e+ele in dic or ele+e in dic:
      return True
  return False

T = int(raw_input())
for case in range(T):
  val = raw_input().split(' ')
  C = int(val[0])
  combination = dict([(comb[:2],comb[2]) for comb in val[1:C+1]])
  D = int(val[C+1])
  opposition = set(val[C+2:C+D+2])
  N = int(val[C+D+2])
  elements = val[C+D+3]
  res = []
  for e in elements:
    if not res:
      res.append(e)
    else:
      last = res.pop()
      if last+e in combination:
        res.append(combination[last+e])
      elif e+last in combination:
        res.append(combination[e+last])
      else:
        res.append(last)
        if check_opposed(res, e, opposition):
          res = []
        else:
          res.append(e)
  print 'Case #%i: [%s]' %(case+1, ', '.join(res))
