#!/usr/bin/python

from sys import stdin
from math import ceil, floor

def signum(x):
  if x < 0: return -1
  else:     return 1

def evaluate_case(mass, height, width, matrix):
  for size in range(min(height, width), 2, -1):
    edge_lower = floor(size / 2)
    edge_upper = ceil(size / 2)
    _diff = 1 - (edge_upper - edge_lower)
    
    cxr = range(edge_lower, width - edge_lower + _diff)
    cyr = range(edge_lower, height - edge_lower + _diff)

    for cx in cxr:
      for cy in cyr:
        sx = 0
        sy = 0
    
        dxr = range(-edge_lower, edge_upper)
        dyr = range(-edge_lower, edge_upper)
          
        for dx in dxr:
          for dy in dyr:
            if size % 2 == 0:
              _dx = dx + 0.5
              _dy = dy + 0.5
            else:
              _dx = dx
              _dy = dy
            
            u, l = edge_lower, -edge_lower
            
            if size % 2 == 0:
              u -= 1
              
            if (dx != l and dx != u) or (dy != l and dy != u):
              m = mass + matrix[cy + dy][cx + dx]
              sx += _dx * m
              sy += _dy * m

        if sx == 0 and sy == 0:
          return size

  return "IMPOSSIBLE"

def read_list(n):
  lines = []
  for _ in range(n):
    line = stdin.readline().strip()
    lines.append(tuple(map(int, line)))
  return lines
  
count = int(stdin.readline())

for i in range(1, count+1):
  height, width, mass = map(int, stdin.readline().split())
  matrix = read_list(height)
  
  t = evaluate_case(mass, height, width, matrix)
  print('Case #' + str(i) + ': ' + str(t))
