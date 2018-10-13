#!/usr/bin/env python
# encoding: utf-8
#Python 2.7.2 (v2.7.2:8527427914a2)
#[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin

"""
Problem1A.py

Created by Jawad Rashid on 2012-04-28.
Copyright (c) 2012 Jawad Rashid. All rights reserved.
"""

import sys
import os
import itertools
inputFileName = "A-small-attempt0.in"
inputFile = open(inputFileName, 'r')
outputFile = open("output_" + inputFileName, 'w')

def solveCurrentCase(index):
  result = 0.0
  Probabilities = []
  
  metaData = inputFile.readline().split(" ")
  A = int(metaData[0])
  B = int(metaData[1])
  
  probArr = inputFile.readline().split(" ")
  for i in range(A):
    Probabilities.append(float(probArr[i]))
  
  characterComb = list(itertools.product([0, 1], repeat=A))
  
  #print list(characterComb)
  
  errorProb = []
  
  for eachComb in characterComb:
    error = 1.0
    i = 0
    for eachTuple in eachComb:
      if eachTuple == 0:
        error *= (1 - Probabilities[i])
      else:
        error *= (Probabilities[i])
      i += 1
    errorProb.append(error)
  
  keepTrying = []
  ENTER = 1
  BACKSPACE = 1
  ENTERRIGHTAWAY = 1
  keepTryingExpected = 0.0
  enterRightAway = 0.0
  expected = []
  backSpaceRecord = [0.0] * A
  
  for i in range(len(errorProb)):
    if i == (len(errorProb) - 1): #No Mistakes
      keepTryingExpected += errorProb[i] * (B-A+ENTER)
    else:
      keepTryingExpected += errorProb[i] * (B-A+ENTER+B+ENTER)
    enterRightAway += errorProb[i] * (ENTER+B+ENTER)
    for j in range(len(backSpaceRecord)):
      no_of_backspaces = j+1
      currentComb = characterComb[i][:len(characterComb[i]) -no_of_backspaces]
      if len(currentComb) == 0 or not (0 in currentComb):
        value =  2 * no_of_backspaces + (B-A) + ENTER
      else:
        value =  2 * no_of_backspaces + (B-A) + ENTER + B + ENTER
      backSpaceRecord[j] += errorProb[i] * value
      #print currentComb
  expected.append(keepTryingExpected)
  expected.append(enterRightAway)
  result =  min(min(backSpaceRecord), min(expected))
  
  output = "Case #" + str(index+1) + ": " + "{:f}".format(result)
  print output
  outputFile.write(output+"\n")
  
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


