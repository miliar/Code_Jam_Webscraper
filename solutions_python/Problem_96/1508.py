#!/usr/bin/python
import string

allTheLetters = string.lowercase

def debug(message):
  print message



#slow way :p
def canMeetBestNormal(totalscore, atLeast):
  for s1 in range(0,11):
    for s2 in range(0,11):
      for s3 in range(0,11):
        if isNormalTriplet(s1, s2, s3):
          if match(s1, s2, s3, totalscore, atLeast):
            return True


#slow way :p
def canMeetBestSurprising(totalscore, atLeast):
  for s1 in range(0,11):
    for s2 in range(0,11):
      for s3 in range(0,11):
        if isSurprisingTriplet(s1, s2, s3):
          if match(s1, s2, s3, totalscore, atLeast):
            return True



def match(s1, s2, s3, totalscore, atLeast):
  if (s1+s2+s3 != totalscore):
    return False
  
  if (s1>=atLeast):
    return True
  if (s2>=atLeast):
    return True
  if (s3>=atLeast):
    return True
  return False

#only 1 apart
def isNormalTriplet(s1, s2, s3):
  if (abs(s1-s2)>1):
    return False
  if (abs(s1-s3)>1):
    return False
  if (abs(s2-s3)>1): #not needed
    return False
  return True

#is 2 apart
def isSurprisingTriplet(s1, s2, s3):
  if isNormalTriplet(s1, s2, s3):
    return False
  
  if (abs(s1-s2)>2):
    return False
  if (abs(s1-s3)>2):
    return False
  if (abs(s2-s3)>2): #not needed
    return False
  
  return True




print "start"

outfile=open('outDance','w')

infile=open('in','r')

infile.readline()

caseNumber=0

for line in infile:

    caseNumber+=1
    
    line=line.rstrip('\n');
    
    inputs=line.split(" ")
    
    print inputs
    
    
    numberOfGooglers=int(inputs[0])
    surprisingTriplets=int(inputs[1])
    atLeast=int(inputs[2])
    
    
    totalPoints=[]
    
    for i in range(0,numberOfGooglers):
      totalPoints.append(int(inputs[3+i]))
    
    
    currentSurprisingTriplets=surprisingTriplets
    currentMaximumNumber=0
    
    for googler in totalPoints:
      
      if canMeetBestNormal(googler, atLeast):
        currentMaximumNumber += 1
        continue
      
      if currentSurprisingTriplets>0:
        if canMeetBestSurprising(googler, atLeast):
          currentMaximumNumber += 1
          currentSurprisingTriplets -= 1
          continue
    
    
    outputLine=str(currentMaximumNumber)
    
    outLine="Case #"+str(caseNumber)+": "+outputLine
    
    print outLine
    outfile.write(outLine+"\n")







