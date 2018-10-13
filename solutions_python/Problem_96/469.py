#!/usr/bin/env python
# encoding: utf-8
#Python 2.7.2 (v2.7.2:8527427914a2)
#[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin

"""
Dancing With The Googlers.py

Created by Jawad Rashid on 2012-04-14.
Copyright (c) 2012 Jawad Rashid. All rights reserved.
"""

import sys
import os
inputFileName = "B-large.in"
inputFile = open(inputFileName, 'r')
outputFile = open("output_" + inputFileName, 'w')

def solveCurrentCase(index):
  googlersScore = []
  atLeastNum = 0
  metaData = inputFile.readline().strip("\n").split(" ")
  N = int(metaData[0])
  S = int(metaData[1])
  p = int(metaData[2])
  
  for i in range(0, N):
     googlersScore.append(int(metaData[i+2+1]))
     
  for i in range(0, N):
    quotient = googlersScore[i] / 3
    remainder = googlersScore[i] % 3
    
    if quotient >= p or ((quotient == (p-1)) and remainder > 0):
      atLeastNum += 1
    elif (S > 0) and (((quotient == (p-1)) and (remainder == 0) and (quotient != 0)) or ((quotient == (p-2)) and (remainder == 2))):
      if index == 6:
        print S
      atLeastNum += 1
      S = S - 1
      
  output = "Case #" + str(index+1) + ": " + str(atLeastNum)
  print output
  outputFile.write(output + "\n")
  
def solveCases():
  T = int(inputFile.readline())
  
  for i in range(0, T):
    solveCurrentCase(i)
    
def main():
    solveCases()
    inputFile.close()
    outputFile.close()
    pass

if __name__ == '__main__':
    main()


