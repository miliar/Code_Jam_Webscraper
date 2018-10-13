#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
from operator import itemgetter
import math

def solve(D, N, K, S):
  t = float(D - K[0]) / float(S[0])
  for i in xrange(1, len(K)):
    t = max(t, float(D - K[i]) / float(S[i]))
  return float(D) / t

def main():
  
  # Open the file to read
  file = open("Test.txt", "r")
  
  # Read the file
  T = int(file.readline())
  answer = []

  # Read the cases
  for i in xrange(T):
    D, N = file.readline().split(' ')
    D, N = int(D), int(N)
    K, S = [], []
    for n in xrange(N):
      k, s = file.readline().split(' ')
      K.append(int(k))
      S.append(int(s))
    
    print K, S
    
    # Solve them
    answer.append("Case #" + str(i + 1) + ": " + str(solve(D, N, K, S)) + "\n")
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