#!/usr/bin/env python

T = int(raw_input())

for x in range(1, T+1):
  first = int(raw_input())
  for j in range(1,5):
    row = map(int, raw_input().split())
    if j == first:
      firstRow = set(row)
  second = int(raw_input())
  for j in range(1,5):
    row = map(int, raw_input().split())
    if j == second:
      secondRow = set(row)
  common = firstRow & secondRow
  if len(common) == 0:
    print "Case #"+str(x)+": Volunteer cheated!"
  elif len(common) == 1:
    print "Case #"+str(x)+": "+str(common.pop())
  else: 
    print "Case #"+str(x)+": Bad magician!"

