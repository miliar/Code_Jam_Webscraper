#!/usr/bin/env python
import sys
import pprint

class RecycledNumber:
  def __init__(self, num):
    self.num = num

  @staticmethod
  def shiftLeft(inputStr):
    if (inputStr is None or inputStr == ''):
      return ''

    if (len(inputStr) == 1):
      return inputStr

    return inputStr[1:] + inputStr[0]

  def getRecycledCombinations(self, min, max):
    origNumStr = str(self.num)
    numStr = str(self.num)
    recycledCombinations = set()

    for i in range(0, len(numStr)-1):
      numStr = RecycledNumber.shiftLeft(numStr)

      if (not numStr.startswith('0')):
        num = int(numStr)
        if (num >= min and num <= max and origNumStr != numStr):
          recycledNumberPair = frozenset([origNumStr, numStr])
          recycledCombinations.add(recycledNumberPair)

    return recycledCombinations

class RecycledNumberRange:
  def __init__(self, startNum, endNum):
    self.startNum = startNum
    self.endNum = endNum

  def getRecycledCombinations(self):
    allRecycledCombinations = set()

    for i in range(self.startNum, self.endNum+1):
      recycledNumber = RecycledNumber(i)
      recycledCombinations = recycledNumber.getRecycledCombinations(self.startNum, self.endNum)
      allRecycledCombinations = allRecycledCombinations.union(recycledCombinations)

    return allRecycledCombinations

  @staticmethod
  def makeFromInputLine(inputLine):
    data = inputLine.split()

    return RecycledNumberRange(int(data[0]), int(data[1]))

  def getRecycledCombinationsCnt(self):
    return len(self.getRecycledCombinations())

def readFromStdin():
  data = sys.stdin.readlines()

  return data

def readFromFile(filename):
  f = open(filename)
  data = f.readlines()
  f.close()
  
  return data

def main():
  if len(sys.argv) >= 2 and sys.argv[1] != '-':
    data = readFromFile(sys.argv[1])
  else:
    data = readFromStdin()

  numOfTestCases = int(data[0])

  assert (numOfTestCases == len(data)-1), "invalid data file"

  for i in range(1, len(data)):
    recycledNumberRange = RecycledNumberRange.makeFromInputLine(data[i])
    print "Case #%d: %d" % (i, recycledNumberRange.getRecycledCombinationsCnt())

if __name__=="__main__":
  main()
