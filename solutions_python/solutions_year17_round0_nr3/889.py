#!/usr/bin/env python3

import math
from sys import stdin as I

def solve(T):
  N, K = map(int, I.readline().split())

  spaces = {N: 1}
  spaceCount = 1

  while K > spaceCount:
    newSpaces = {}
    for space in spaces:
      size = math.ceil((space - 1) / 2.0)
      if not size in newSpaces:
        newSpaces[size] = 0
      newSpaces[size] += spaces[space]
      size = math.floor((space - 1) / 2.0)
      if not size in newSpaces:
        newSpaces[size] = 0
      newSpaces[size] += spaces[space]
    K -= spaceCount
    spaceCount *= 2
    spaces = newSpaces

  largest = max(spaces.keys())
  size = largest if K <= spaces[largest] else largest - 1
  print("Case #%i: %i %i" % (T, math.ceil((size - 1) / 2.0), math.floor((size - 1) / 2.0)))

T = int(I.readline())
for i in range(T):
  solve(i + 1)
