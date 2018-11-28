#!/usr/bin/python
import sys
T = int(sys.stdin.readline())
for case in range(1,T+1):
  answer1 = int(sys.stdin.readline())
  rows=[]
  for i in range(1,5):
    rows.append(map(int,sys.stdin.readline().strip().split()))
  candidates1=set(rows[answer1-1])

  answer2 = int(sys.stdin.readline())
  rows=[]
  for i in range(1,5):
    rows.append(map(int,sys.stdin.readline().strip().split()))
  candidates2=set(rows[answer2-1])
  final = list(candidates1.intersection(candidates2))
  if len(final) < 1: solution = "Volunteer cheated!"
  if len(final) > 1: solution = "Bad magician!"  
  if len(final) == 1: solution = final[0]
  print "Case #%i: %s" % (case,solution)
