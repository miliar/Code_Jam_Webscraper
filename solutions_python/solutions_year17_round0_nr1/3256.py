#! /usr/bin/env python

import sys

def parse(lines):
  n = int(lines[0])
  cakes = []
  for i in range(n):
    cakes.append((list(lines[i+1].split(" ")[0]), int(lines[i+1].split(" ")[1])))
  return cakes
  
def solve(cake):
  num = 0
  k = cake[1]
  n = len(cake[0])
  for i in range(n):
    if (cake[0][i] == '-'):
      if (i > n - k):
        return "IMPOSSIBLE"
      else:
        for j in range(i, i+k):
          if (cake[0][j] == '+'):
            cake[0][j] = '-'
          else:
            cake[0][j] = '+'
        num = num + 1
  return str(num)
    
with open(sys.argv[1], 'r') as f:
  cakes = parse(f.read().splitlines())
for i in range(len(cakes)):
  sol = solve(cakes[i])
  print "Case #" + str(i+1) + ": " + sol
