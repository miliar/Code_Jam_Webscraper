#!/usr/bin/python

from sys import argv
from math import sqrt

if len(argv) > 1:
  filename = argv[1]
else:
  filename = "test.in"

f = open(filename)

numCases = int(f.readline())

def allPerms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in allPerms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def applyPermutation(string, perm):
  newStr = " "*len(string)
  c = 0
  for x in perm:
    newStr = newStr[:c] + string[x] + newStr[c+1:]
    c+=1
  return newStr

def applyAllPermutation(string, perm):
  newStr = ""
  leng = len(perm)
  for x in range(len(string)/leng):
    newStr += applyPermutation(string[x*leng:(x+1)*leng], perm)
  return newStr

def compressValue(string):
  char = ""
  count = 0
  for x in string:
    if char != x:
      char = x
      count += 1
  return count

for case in range(1, numCases + 1):
  output = ""
  k = int(f.readline())
  string = f.readline().strip()
  perms = allPerms(range(0, k))
  
  sol = []
  
  for perm in perms:
    sol.append(compressValue(applyAllPermutation(string, perm)))

  sol.sort()
  
  output = str(sol[0])
  #x1, y1, x2, y2, x3, y3 = map(lambda x:int(x), f.readline().split())

  print "Case #"+str(case)+": "+ output
