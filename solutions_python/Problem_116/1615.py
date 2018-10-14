#!/usr/bin/python

import sys
from sets import Set

f = open(sys.argv[1]);
out = open(sys.argv[1] + ".out.txt", "w");

dim = 4

def compute(arr):
  def checkdir(i, j, ii, jj):
    l = [arr[i + c*ii][j + c*jj] for c in range(dim)]
    if all(map(lambda x: x=='X' or x=='T', l)):
      return "X won"
    if all(map(lambda x: x=='O' or x=='T', l)):
      return "O won"
    return 0
  
  for i in range(dim):
    r = checkdir(i, 0, 0, 1)
    if r != 0:
      return r
    r = checkdir(0, i, 1, 0)
    if r != 0:
      return r

  r = checkdir(0, 0, 1, 1)
  if r != 0:
    return r
  r = checkdir(0, 3, 1, -1)
  if r != 0:
    return r

  if any([x=="." for x in l for item in [[3], [4]]]):
    return "Game has not completed"
  
  return "Draw"

num = int(f.readline());

for i in range(1,num+1):

  arr = []
  for j in range(dim):
    l = f.readline().strip()
    arr.append(l)
  f.readline()

  result = compute(arr)

  s = "Case #" + str(i) + ": " + str(result)
  print s
  out.write(s + "\n");

f.close();
out.close();