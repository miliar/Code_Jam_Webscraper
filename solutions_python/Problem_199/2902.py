#!/usr/bin/python
from __future__ import print_function
import sys

def flipPancakes(chi,k) :
  res = 0
  s = list(ch)
  for i in range(0,len(s)):
    if s[i] == "-" and i+int(k) <= len(s):
      res = res + 1 
      for j in range(0,int(k)):
        if s[i+j] == "+":
           s[i+j] = "-"
        else:
           s[i+j] = "+"
  if '-' in s:
    res = "IMPOSSIBLE"
  return res


file = open(sys.argv[1],'r') 
totalCase = int(file.readline())
caseNumber = 1

while caseNumber <= totalCase:
  print ('Case #' + str(caseNumber) + ': ',end='')
  toAnalyze = file.readline().split()
  ch = toAnalyze[0]
  K = toAnalyze[1]
  res = flipPancakes(ch,K)
  print (res)
  caseNumber += 1

