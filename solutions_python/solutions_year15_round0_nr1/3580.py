#!/bin/python

def solve(case_num):
  shyness = [int(i) for i in raw_input().split(' ')[1]]
  additional = 0
  total_so_far = shyness[0]
  for i in range(1, len(shyness)):
    increase = max(i - total_so_far, 0)
    additional += increase
    total_so_far += (shyness[i] + increase)
    
  print 'Case #' + str(case_num) + ': ' + str(additional)

T = raw_input()
for i in range(int(T)):
  solve(i+1)
