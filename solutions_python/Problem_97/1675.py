#!/usr/bin/python
import sys

def rotations(n):
  l = []
  sn = list(str(n))
  for _ in range(len(sn)-1):
    sn.insert(0,sn.pop(len(sn)-1))
    if sn[0] != '0':
      l.append(int(''.join(sn)))
  return list(set(l))

def countPairs(A,B):
  count = 0
  for n in range(A,B):
    l = rotations(n)
    l = filter(lambda m: n<m and m<=B,l)
    count = count + len(l)
  return count


T = int(sys.stdin.readline())

counter = 1
for line in sys.stdin:
  case = line.rstrip().split()
  A = int(case[0])
  B = int(case[1])
  print "Case #{0}: {1}".format(counter,countPairs(A,B))
  counter = counter + 1

