#!/usr/bin/env python
# encoding: utf-8
#Python 2.7.2 (v2.7.2:8527427914a2)
#[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin

"""
Recycle Numbers.py

Created by Jawad Rashid on 2012-04-14.
Copyright (c) 2012 Jawad Rashid. All rights reserved.
"""

import sys
import os
import math
inputFileName = "C-large.in"
inputFile = open(inputFileName, 'r')
outputFile = open("output_" + inputFileName, 'w')

#Finds the length could have used len(str(integer)) but this function is more better
def findLength(integer):
  if integer == 0:
    return 1
  else:
    return int(math.log10(integer))+1

def checkSameNumbers(number, digits):
  strVer = str(number)
  sameElem = strVer[0]
  
  for i in range(1, digits):
    if strVer[i] != sameElem:
      return False
      
  return True

#Checks if the current number is recycble or not
#-1 = Unchanged or unrecyble
#0 = Recyble
#1 = Condition
def checkRecycbleNumber(number, rotations, A, B, digits, recyblePairs):
  currentNumStr = str(number)
  maxNumStr = str(B)
  if currentNumStr[-rotations] == "0":
    return -1
  if int(currentNumStr[digits - rotations:digits]) > int(maxNumStr[0:rotations]):
    newNum = int(str(int(currentNumStr[0:digits - rotations]) + 1) + str("0"*rotations))
    return newNum
  else:
    start = currentNumStr[0:digits - rotations]
    end = currentNumStr[digits - rotations:]
    newNum = int(end + start)
    if findLength(newNum) != digits:
      return -1
    else:
      if newNum <= B:
        #if checkSameNumbers(number, digits):
        #  return -1
        #Recyble Found
        if recyblePairs.has_key(str(number)+","+str(newNum)):
          return -1
        if number == newNum:
          return -1
        if number > B or newNum > B or number < A or newNum < A:
          return -1
        recyblePairs[str(number)+","+str(newNum)] = 1
        recyblePairs[str(newNum)+","+str(number)] = 1
        return 0
    
  return -1

#Finds the number of recycbles between A and B
def findRecycles(A, B, digits, recyblePairs):
  count = 0

  #Shift by 1, 2, 3, 4...
  for i in range(1, digits):
    #print "\n\n" + str(i),
    currentNum = A
    while currentNum <= B:
      outputType = checkRecycbleNumber(currentNum, i, A, B, digits, recyblePairs)
      if outputType == 0 or outputType == -1:
        currentNum = currentNum + 1
        if outputType == 0:
          count += 1
      else:
        currentNum = outputType
    else:
      currentNum = currentNum + 1
  
  #print recyblePairs
  
  return count

#Solve the case by reading A, B
def solveCurrentCase(index):
  metaData = inputFile.readline().split(" ")
  A = int(metaData[0])
  B = int(metaData[1])
  
  count = 0
    
  digits = findLength(A)
  recyblePairs = {}
  #1 digit number are not recycables
  if digits > 1:
    count = findRecycles(A, B, digits, recyblePairs)
    
    
  output = "Case #" + str(index+1) + ": " + str(count)
  #print "\n"
  print output
  #print "\n"
  
  outputFile.write(output + "\n")

#Finds T  
def solveCases():
  T = int(inputFile.readline())
  
  for i in range(0, T):
    solveCurrentCase(i)

#Start Here    
def main():
    solveCases()
    inputFile.close()
    outputFile.close()
    pass

if __name__ == '__main__':
    main()


