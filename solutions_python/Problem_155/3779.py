#Case #1: 0

#0,1,2,3,4,5,6
#1,1,1,1,1
#0,9
#1,1,0,0,1,1
#0,0,0,8,0,4,1
#2,3,0,0,0,1
#0,0,0,0,0,0,1
#2,2,1
#0,0,0,0,3,3,1
#3,5,2,0,0,0,1
#1
#9,4,9,2,4,7,2

from __future__ import print_function

def getInjectCount(shynessData):
  standing = 0;
  injectCnt = 0;
  for shyness, personCnt in enumerate(shynessData):
    #print(shyness, standing, injectCnt)
    if shyness>standing and personCnt>0:
      injectCnt += shyness - standing
      standing += injectCnt
    standing += personCnt
  return injectCnt


def outputGen(fileName, resultList):
  with open(fileName + '.output', 'w') as f:
    for idx, val in enumerate(resultList):
      print("Case #"+ str(idx+1) + ": " + str(val), file=f)

def execute(fileName):
  resultList = []
  with open(fileName, 'r') as f:
    no_of_cases = int(f.readline())
    for line in f:
      resultList.append(handleEachCase(line))
  outputGen(fileName, resultList)


def handleEachCase(caseData):
  s_max = caseData.split(' ')[0]
  shynessData = map(lambda x: int(x), list(caseData.split(' ')[1])[:-1])
  return getInjectCount(shynessData)

import sys
fileName = sys.argv[1]
execute(fileName)
