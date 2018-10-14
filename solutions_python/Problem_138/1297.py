#!/usr/bin/python
import os,sys
T=int(raw_input())
for t in range(T):
  N = int(raw_input())
  rowA = sorted([float(e) for e in raw_input().split()])
  rowB = sorted([float(e) for e in raw_input().split()])

  # strat A
  ia = 0
  res = 0
  for b in rowB:
    while ia<len(rowA) and  b>rowA[ia]:
      ia += 1
    if ia>=len(rowA):
      break
    res+=1
    ia+=1

  # strat B
  rowA.reverse()
  ibend = len(rowB)-1
  ibbegin = 0
  res2 = 0
  for a in rowA:
    if a>rowB[ibend]:
      res2 += 1
      ibbegin += 1
    else:
      ibend -= 1
  
  print 'Case #'+str(t+1)+': '+str(res)+' '+str(res2)

