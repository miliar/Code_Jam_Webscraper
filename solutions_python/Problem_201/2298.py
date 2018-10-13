#!/usr/bin/python
from __future__ import print_function
import sys

def isTidy(i):
  res = 1
  ch = list(i)
  for i in range(0,len(ch)-1):
    if int(ch[i]) <= int(ch[i+1]):
      continue
    else:
      res = 0 
      break 
  return res

def chooseNext(num):
  res = int(num) - 1
  ch = list(num)
  for i in range(0,len(ch)-1):
    if int(ch[i]) <= int(ch[i+1]):
      continue
    else:
      ind = i+1
      totalDigitToIgnore = len(ch) - (ind + 2)
      if str(ch[len(ch)-1]) == str('0'):
        res = int(num) - 1
      else:
        res = int(num)  - max(10**totalDigitToIgnore,1) 
      break

  return res


file = open(sys.argv[1],'r') 
totalCase = int(file.readline())
caseNumber = 1
res = 0
while caseNumber <= totalCase:
  print ('Case #' + str(caseNumber) + ': ',end='')
  toAnalyze = int(file.readline())
  end = 0
  currentTest = toAnalyze
  while not end:
    if isTidy(str(currentTest)):
      res=currentTest
      print(res)
      end = 1
    else:
      currentTest = chooseNext(str(currentTest))

  caseNumber += 1

