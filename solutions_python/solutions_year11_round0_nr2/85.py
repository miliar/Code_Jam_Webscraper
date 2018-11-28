#!/usr/bin/python

import sys

def readInput():
  file = open(sys.argv[1])

  testCaseCount = int(file.readline().rstrip())

  testCases = [file.readline().rstrip().split() for line in xrange(testCaseCount)]
  
  return testCases

def solve(line):
  index = 0

  nonBaseCount = int(line[index])
  index += 1

  nonBases = line[index:index+nonBaseCount]
  nonBaseDict = {}
  for nonBase in nonBases:
    nonBaseDict[nonBase[0:2]] = nonBase[2]
    nonBaseDict[nonBase[1] + nonBase[0]] = nonBase[2]
  index += nonBaseCount

  opposeCount = int(line[index])
  index += 1

  opposes = line[index:index+opposeCount]
  opposesDict = {}
  for oppose in opposes:
    if oppose[0] not in opposesDict:
      opposesDict[oppose[0]] = set()
    if oppose[1] not in opposesDict:
      opposesDict[oppose[1]] = set()

    opposesDict[oppose[0]].add(oppose[1])
    opposesDict[oppose[1]].add(oppose[0])

  index += opposeCount

  invokeCount = int(line[index])
  index += 1

  elementList = []
  elements = {}

  for element in line[index]:
    elementList.append(element)
    if element not in elements:
      elements[element] = 0
    elements[element] += 1

    if len(elementList) == 1:
      continue
    combination = elementList[-2] + elementList[-1]
    if combination in nonBaseDict:
      elements[elementList.pop()] -= 1
      elements[elementList.pop()] -= 1
      elementList.append(nonBaseDict[combination])
    elif elementList[-1] in opposesDict:
      for oppose in opposesDict[elementList[-1]]:
        if oppose in elements and elements[oppose] > 0:
          elementList = []
          elements = {}
          break

  return elementList

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
  print 'Case #%d: [%s]' % (testCaseNr, ', '.join(solve(testCase)))
  testCaseNr += 1
