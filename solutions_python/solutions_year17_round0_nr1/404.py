#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
from operator import itemgetter
import math

def flip(pancakes, k, i):
  if i + k - 1 < len(pancakes):
    for j in xrange(k):
      pancakes[i + j] = '+' if pancakes[i + j] == '-' else '-'

def solve(pancakes, k):
  nbFlip = 0
  for i in xrange(len(pancakes)):
    if pancakes[i] == '-':
      if i + k > len(pancakes):
        return "IMPOSSIBLE"
      flip(pancakes, k, i)
      nbFlip += 1
      
  return str(nbFlip) if pancakes[-1] == '+' else "IMPOSSIBLE"

def main():
  # Open the file to read
  file = open("test.txt", "r")
  
  # Read the file
  N = int(file.readline())
  answer = []

  # Read the cases
  for i in xrange(N):
    s, k = file.readline().split(' ')
    
    # Solve them
    answer.append(solve(list(s), int(k)))
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