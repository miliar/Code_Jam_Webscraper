#!/usr/bin/env python
#Python 2.7.2 (v2.7.2:8527427914a2)
#[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# encoding: utf-8
"""
Speaking in Tongues

Created by Jawad Rashid on 2012-04-14.
Copyright (c) 2012 Jawad Rashid. All rights reserved.
* Sorting Code for keys and value for dictionary taken from http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
"""

import sys
import os
inputFileName = "A-small-attempt0.in"
inputFile = open(inputFileName, 'r')
outputFile = open("output_" + inputFileName, 'w')
#Example used to find mapping
trainingData = [{"google":"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
                  "original":"our language is impossible to understand"},
                  {"google":"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                   "original":"there are twenty six factorial possibilities"},
                   {"google":"de kr kd eoya kw aej tysr re ujdr lkgc jv",
                    "original":"so it is okay if you want to just give up"}]
#Initial Mapping from problem statement
mapping = {"y":"a", "e":"o","q":"z"}

def getMappingForChar(googleChar):
  if googleChar == " ":
    return googleChar
  else:
    return mapping[googleChar]
  
#Solve one case using the mapping
def solveCurrentCase(index):
  googleText = inputFile.readline().strip("\n")
  originalText = ""
  
  output = "Case #" + str(index+1) + ": "
  for i in range(0, len(googleText)):
    googleChar = googleText[i]
    originalChar = getMappingForChar(googleChar)
    originalText = originalText + originalChar
  
  output = output + originalText
  print output
  outputFile.write(output + "\n")
  
#Solve all cases 
def solveCases():
  T = int(inputFile.readline())
  
  for i in range(0, T):
    solveCurrentCase(i)

#If the mapping for a character is not already done then inserts a new mapping for the google character and the origonal character
def insertMapping(google, original):
    if not(mapping.has_key(google)) and original != " " :
      mapping[google] = original

#Sort and print mapping by keys      
def printMappingSortedByKeys():
  for key in sorted(mapping.iterkeys()):
    print "%s: %s" % (key, mapping[key])

#Sort and print mapping by values   
def printMappingSortedByValue():
  for key, value in sorted(mapping.iteritems(), key=lambda (k,v): (v,k)):
      print "%s: %s" % (key, value)

#Find the missing mapping  
def findMissingMapping():
  #97 ascii for 'a' and 97+25 ascii for 'z'
  googleMissing = ''
  originalMissing = ''
  googleFlag = False
  originalFlag = False
  mappingValues = mapping.viewvalues()
  mappingKeys = mapping.viewkeys()
  
  for i in range(97, 97+26):
    char = chr(i)
    
    if not googleFlag:
      if not char in mappingKeys:
        googleMissing = char
        googleFlag = True

    if not originalFlag:
      if not char in mappingValues:
        originalMissing = char
        originalFlag = True
    
    if googleFlag and originalFlag:
      break
  
  insertMapping(googleMissing, originalMissing)
  
#Creates mapping from the example data and fills in the last missing mapping  
def createMappingTable():
    for eachExample in trainingData:
      googleText = eachExample["google"]
      actualText = eachExample["original"]
      textLength = len(googleText)
      
      for i in range(0, textLength):
        googleChar = googleText[i]
        actualChar = actualText[i]
        if googleChar != " ":
          insertMapping(googleChar, actualChar)
    
    findMissingMapping()
    #print mapping
    #Find Missing Mapping
    #print "Mapping from Google To Original Text"
    #printMappingSortedByKeys()
    #print "\n"
    #printMappingSortedByValue()
    #print len(mapping.keys())

#Creates mapping from the example data and solve the input cases based on that    
def main():
    createMappingTable()
    solveCases()
    inputFile.close()
    outputFile.close()
    pass

if __name__ == '__main__':
    main()


