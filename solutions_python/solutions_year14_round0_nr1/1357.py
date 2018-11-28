#!/usr/bin/python
import os,sys
T=int(raw_input())
for t in range(T):
  rowsA=[]
  rowsB=[]
  lineA = int(raw_input())
  for i in range(4):
    rowsA.append([int(e) for e in raw_input().split()])
  lineB = int(raw_input())
  for i in range(4):
    rowsB.append([int(e) for e in raw_input().split()])

  # find common ints
  a = rowsA[lineA-1]
  b = rowsB[lineB-1]
  res = []
  for i in range(4):
    for j in range(4):
      if a[i] == b[j]:
        res.append(a[i])

  if len(res) == 1:
    print 'Case #'+str(t+1)+': '+str(res[0])
  elif len(res) == 0:
    print 'Case #'+str(t+1)+': Volunteer cheated!'
  else:
    print 'Case #'+str(t+1)+': Bad magician!'

