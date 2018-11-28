#!/usr/bin/python
import string
import math

def debug(message):
  print message

def log(message):
  print message

def getCount(start, end):
  count=0
  for number in xrange(start, end+1):
    if (isPalindrome(number) and isSquarePalindrome(number)):
      count+=1
  return count

def isPalindrome(number):
  string='%.12g' % number
  return string==string[::-1]

def isSquarePalindrome(number):
  square=math.sqrt(number)
  return isPalindrome(square);

log("start")
outfile=open('outFair','w')
infile=open('in','r')
infile.readline()

caseNumber=0
for line in infile:
  caseNumber+=1
  
  line=line.rstrip('\n');
  inputs=line.split(" ")
  
  count=getCount(int(inputs[0]), int(inputs[1]))
  
  outputLine=str(count)
  outLine="Case #"+str(caseNumber)+": "+outputLine
  outfile.write(outLine+"\n")




