#!/usr/bin/python

from sys import stdin

def evaluate_case(n, Pd, Pg):
  if Pg == 100 and Pd < 100:
    return 'Broken'

  if Pg == 0 and Pd > 0:
    return 'Broken'

  for d in range(min(100, n) + 1):
    Wd = (d * Pd) / 100

    if Wd == int(Wd) and (Wd > 0 or Pd == 0):
      return 'Possible'
    
  return 'Broken'

cases = stdin.readlines()
count = int(cases[0])

for i in range(1, count+1):
  n, Pd, Pg = (int(x) for x in cases[i].split())
  print('Case #' + str(i) + ': ' + evaluate_case(n, Pd, Pg))
