#!/usr/bin/python
import math
import time

def isPalindrome(number):
  # Palindrome means that it is simetric
  isPalindrome=1
  i=-1
  j=len(str(number))
  while i<(len(str(number))-1) and isPalindrome==1:
    i=i+1
    j=j-1
    #print "i: "+str(i)
    #print "j: "+str(j)
    if str(number)[i]!=str(number)[j]:
      isPalindrome=0

  return isPalindrome

def isPerfectSquare(number):
  # Perfect square means that its decimal is 0
  perfectSquare=0
  if str(math.sqrt(number)).split('.')[1]=="0":
    perfectSquare=1
  else:
    perfectSquare=0
  return perfectSquare


# Open input file
inputF=open('C-small-attempt1.in','r')
outputF=open('C-small-attempt1.out','w')
# Get number of cases
line=""
while len(line)<1:
  line=inputF.readline()
NoC=int(line)
#print NoC

# Read all cases and solve it
case=0
while case<NoC:
  case=case+1
  line=inputF.readline()
  while len(line)<1:
    line=inputF.readline()
  caseLine=line
  #print caseLine
  rangeBegins=int(caseLine.split()[0])
  rangeEnds=int(caseLine.split()[1])
  print "."
  print case
  print rangeBegins
  print rangeEnds
  # All input data in rangeBegins, rangeEnds and case
  NumberIsFairAndSquare=0
  caseTest=int(rangeBegins)-1
  while int(caseTest) < int(rangeEnds):
    # Test if caseTest is a Fair and perfect Square
    #print "."
    #print "caseTest : "+str(caseTest)
    #print "rangeEnds : "+str(rangeEnds)
    #time.sleep(1)
    caseTest=caseTest+1
    # Perfect square means that its decimal is 0
    if isPerfectSquare(caseTest):
      perfectSquare=int(math.sqrt(caseTest))
      # print str(caseTest)+ "is perfect square"
      #print str(caseTest)+" isPalindrome: "+str(isPalindrome)
      if ((isPalindrome(caseTest)==1) and (isPalindrome(perfectSquare)==1)):
        NumberIsFairAndSquare=NumberIsFairAndSquare+1
        print "Found FairAndSquare: "+str(caseTest)+" with perfectSquare: "+str(perfectSquare)
  outputF.write("Case #"+str(case)+": "+str(NumberIsFairAndSquare)+"\n")
#        print "Case #"+str(case)+": "+str(NumberIsFairAndSquare)

#    #else:
#      #print str(caseTest)+ "is NOT perfect square"
#  print "Number is Fair And Square in range "+str(rangeBegins)+"-"+str(rangeEnds)+" is "+str(NumberIsFairAndSquare)
    
inputF.close()
outputF.close()
