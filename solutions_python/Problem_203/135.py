#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
from operator import itemgetter
import math

def solve(cake, R, C):
  
  for i in xrange(R):
    hasFoundLetter = False
    letter = ''
    for j in xrange(C):
      if cake[i][j] == '?':
        if hasFoundLetter:
          cake[i][j] = letter
      else:
        if hasFoundLetter:
          letter = cake[i][j]
        else:
          hasFoundLetter = True
          letter = cake[i][j]
          k = j - 1
          while k >= 0:
            if cake[i][k] == '?':
              cake[i][k] = letter
              k = k - 1
            else:
              break
  
  hasFoundLine = False
  line = []
  for i in xrange(R):
    if cake[i][0] == '?':
      if hasFoundLine:
        cake[i] = line
    else:
      if hasFoundLine:
        line = cake[i]
      else:
        hasFoundLine = True
        line = cake[i]
        k = i - 1
        while k >= 0:
          if cake[k][0] == '?':
            cake[k] = line
            k = k - 1
          else:
            break
  
  return cake

def main():
  
  # Open the file to read
  file = open("Test.txt", "r")
  
  # Read the file
  T = int(file.readline())
  answer = []  

  # Read the cases
  for i in xrange(T):
    R, C = file.readline().split(' ')
    R, C = int(R), int(C)
    cake = []
    
    for m in xrange(R):
      row = list(file.readline())
      cake.append(row[:-1] if row[-1] == '\n' else row)
      
    # Solve them
    cake = solve(cake, R, C)
    print cake    
    
    answer.append("Case #" + str(i + 1) + ":\n")
    for c in cake:
      answer.append(''.join(c) + "\n")
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