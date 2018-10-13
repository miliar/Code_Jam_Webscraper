#!/usr/local/bin/python2.7
    
f = open('input.txt','r')
line = f.readline().strip()
number_of_cases = int(line)
for case in range(number_of_cases):
  print 'Case #'+str(case+1)+':',
  line = f.readline().strip().split(' ')
  C = float(line[0])
  F = float(line[1])
  X = float(line[2])
  CPS = 2
  total_time = 0
  while True:
    if X/CPS > (C/CPS)+(X/(CPS+F)):
      total_time += C/CPS
      CPS += F
    else:
      total_time += X/CPS
      break
  print round(total_time,7),
  print ''