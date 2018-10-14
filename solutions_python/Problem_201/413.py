#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
from operator import itemgetter
import math

def mergeSet(set):
  newSet = [set[0]]
  for k in xrange(1, len(set)):
    if set[k][0] == newSet[-1][0] and set[k][1] == newSet[-1][1]:
      newSet[-1] = (set[k][0], set[k][1], set[k][2] + newSet[-1][2])
    else:
      newSet.append(set[k])
  
  return newSet
 
def findSet(set, K):
  d, i = 0, 0
  while set[i][2] <= K - d:
    d += set[i][2]
    i += 1

  return set[i][0], set[i][1]

def solve(N, K):
  
  # Initialization
  set = [(N / 2, (N - 1) / 2, 1)]
  step = 1
  #print set
  
  # Build the set until necessary
  while 2 * step <= K:
    newSet = []
    for s in set:
      newSet.append((s[0] / 2, max(s[0]-1, 0)/2, s[2]))
      newSet.append((s[1] / 2, max(s[1] - 1, 0) / 2, s[2]))
    
    set = mergeSet(newSet)
    step *= 2
    #print set
  
  # Find the right value
  #print set, K - step
  l, r = findSet(set, K - step)
  
  return str(l) + " " + str(r)

def main():
  
  # Open the file to read
  file = open("Test.txt", "r")
  
  # Read the file
  T = int(file.readline())
  answer = []  

  # Read the cases
  for i in xrange(T):
    n, k = file.readline().split(' ')
    
    # Solve them
    answer.append(solve(int(n), int(k)))
    print answer[-1]
    
  # Close the file to read
  file.close()
  
  # Write the answer
  file = open("answer.txt", "w")
  for i in xrange(len(answer)):
    file.write("Case #" + str(i + 1) + ": " + answer[i] + "\n")
  file.close()

if __name__ == '__main__':
    main()