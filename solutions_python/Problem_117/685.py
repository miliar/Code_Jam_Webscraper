# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:19:50 2013

@author: LCK

LAWNMOWER addresses the 2nd question in the 2013 Google Code Jam
"""

import numpy as np

# -------- 

#---------


# first, read in the input file
def readInputAndDecide(mypath):
  lines = [line.strip() for line in open(mypath)]

  # turn each line (a str) into a list of ints
  for index, line in enumerate(lines): 
    line = map(int,line.split())
    lines[index] = line # reassignment


# Now go through the test cases
  numTestCases = lines[0][0]
  currentCase = 1 #initialize at 1 bc we're using counting order 
  caseLineBegins = 1 #initialize at 1 bc 1st test case starts at lines[1]
  verdictList = []  
  
  while currentCase <= numTestCases:
    #print lines[caseLineBegins]
    lawnArray = np.array([line for line in lines[(caseLineBegins+1):((caseLineBegins+1)+lines[caseLineBegins][0])]])
   #print lawnArray
    arrayDim = np.array(lines[caseLineBegins])
    verdict = isValidLawn(lawnArray, arrayDim)
    verdictString = "Case #"+str(currentCase)+": "+ verdict
    #print verdictString
    verdictList.append(verdictString)
    caseLineBegins = caseLineBegins+(lines[caseLineBegins][0]+1)
    currentCase +=1
    
  # Write the output file, trashing prev. output.txt files:
    f = open('output.txt','w')
    for verdict in verdictList:
      f.write("%s\n" % verdict)
    f.close()
    
def isValidLawn(lawnArray, arrayDim):

  
  # locate and order the values of the left and bottom edges
  leftBottomDict = dict()  
  # first go down leftmost column
  for index, value in enumerate(lawnArray[:,0]):
    if value in leftBottomDict:
      leftBottomDict[value].append([index,0])
    else:
      leftBottomDict[value] = [[index,0]]
  # next go across the bottom from the 2nd column to end
  for index, value in enumerate(lawnArray[ (arrayDim[0]-1) , 1:arrayDim[1]]):  
    if value in leftBottomDict:
      leftBottomDict[value].append([(arrayDim[0]-1),(index+1)])
    else:
      leftBottomDict[value] = [[arrayDim[0]-1,(index+1)]]
  #print leftBottomDict
  
  # now we are ready to go iterate through dictionary entries
  # get  list of the dictionary values
  validated = 256 
  dictValListUnsorted = []  
  for value in leftBottomDict.iterkeys():
    dictValListUnsorted.append(value)
  dictValList = sorted(dictValListUnsorted)
  for value in dictValList:
    coordList = leftBottomDict[value]
    for coord in coordList:      
      if coord[1] == 0:
        # we are on the left edge, must look across the row
        # 256 is going to be our "validated!" number
        
        #print "on left edge"
        currentRow = lawnArray[coord[0],:]
        #print currentRow
        
        elementCounter = 0
        correctCounter = 0
        #print elementCounter,correctCounter
        for element in currentRow:
          if element == value or element == validated:
            correctCounter += 1;
            elementCounter +=1;
          else:
            elementCounter +=1;
        if elementCounter == correctCounter:
          for index, element in enumerate(currentRow):
            lawnArray[coord[0],index] = validated
        

      if coord[0] == (arrayDim[0] -1):
        #print "on bottom row"
        currentCol = lawnArray[:, coord[1]]
        #print currentCol
        
        elementCounter = 0
        correctCounter = 0
        #print elementCounter,correctCounter
        for element in currentCol:
          if element == value or element == validated:
            correctCounter += 1;
            elementCounter +=1;
          else:
            elementCounter +=1;
        if elementCounter == correctCounter:
          for index, element in enumerate(currentCol):
            lawnArray[index, coord[1]] = validated
  
  print lawnArray

  # Now we will make the verdict based on whether or not all the elements are "256"
  for element in np.nditer(lawnArray):
    if element == 1 :
      return "NO"
  # if we made it this far, we can return YES
  return "YES"
          
    
  

if __name__ == "__main__":
  readInputAndDecide("./B-small-attempt1.in")