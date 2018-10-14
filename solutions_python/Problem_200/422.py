#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import numpy as np
from operator import itemgetter
import math


def solve(k):
  
  for i in xrange(len(k)):
    if i + 1 < len(k) and int(k[i]) > int(k[i + 1]):
      k[i] = str(int(k[i]) - 1)
      for j in xrange(len(k) - i - 1):
        k[i + j + 1] = '9'
      return solve(k if int(k[0]) > 0 else k[1:])       
  
  return ''.join(k)



def solveOld(k):
  s = ""
  print k, len(k)
  for i in xrange(len(k)):
    if i + 1 < len(k) and int(k[i]) > int(k[i + 1]):
      print i, k[i], s
      if int(k[i]) > 1:
        s += str(int(k[i]) - 1)
      for j in xrange(len(k) - i - 1):
        s += "9"
      return s
    else:
      s+= k[i]
    
  return s
    
def main():
  # Open the file to read
  file = open("Test.txt", "r")
  
  # Read the file
  N = int(file.readline())
  answer = []

  # Read the cases
  for i in xrange(N):
    k = list(file.readline())
    
    # Remove the '\n' character
    if (k[-1] == '\n'):
      k = k[:-1]
    
    # Solve them
    answer.append(solve(k))
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