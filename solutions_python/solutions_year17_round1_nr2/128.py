#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
from operator import itemgetter
import math

def getN(R, Q):
  x = Q * 1.0 / (R * 1.1)
  n = int(x)
  r = []
  while n * R * 0.9 <= Q:
    if n * R * 0.9 <= Q and n * R * 1.1 >= Q:
      r.append(n)
    n = n + 1
  return r
  
def getPackage(R, Q):
  r = []
  for q in Q:
    r.append(getN(R, q))
  return r

def solve(N, P, R, Q):

  n = 0
  L = []
  
  for q in xrange(len(Q)):
    L.append(getPackage(R[q], Q[q]))
  
  for l in L[0]:
    if len(l) == 0:
      continue
    g = []
    allFound = True
    for q in xrange(1, len(Q)):
        found = False
        for m in L[q]:
          if len(m) == 0:
            continue
          if (l[0] >= m[0] and l[0] <= m[-1]) or (l[-1] >= m[0] and l[-1] <= m[-1]):
            g.append(m)
            found = True
            break
        if not found:
          allFound = False
          break
    if allFound:
      n = n + 1
      for q in xrange(1, len(Q)):
        L[q].remove(g[q-1])
  
  return n

def main():
  
  # Open the file to read
  file = open("Test.txt", "r")
  
  # Read the file
  T = int(file.readline())
  answer = []  

  # Read the cases
  for i in xrange(T):
    N, P = file.readline().split(' ')
    N, P = int(N), int(P)
    R = [int(r) for r in file.readline().split(' ')]
    print "R = ", R
    Q = []
    
    for n in xrange(N):
      Q.append(sorted([int(q) for q in file.readline().split(' ')]))
    print "Q = ", Q
      
    # Solve them
    answer.append("Case #" + str(i + 1) + ": " + str(solve(N, P, R, Q)) + "\n")
    print answer[-1]
    
  # Close the file to read
  file.close()
  
  # Write the answer
  file = open("answer.txt", "w")
  for a in answer:
    file.write(a)
  file.close()

if __name__ == '__main__':
    main()