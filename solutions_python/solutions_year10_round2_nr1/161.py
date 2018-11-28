import math
import sys

class DirNode:
  def __init__(self, value, parent):
    self.value = value
    if(parent != None):
      parent.children[value] = self
    self.children = {}

  def hasChild(self, value):
    return value in self.children

def addPath(rootNode, path):
  pathList = path.rstrip().split('/')
  #print pathList
  current = rootNode
  addCounter = 0
  for pChunk in pathList:
    if pChunk != "":
      if current.hasChild(pChunk):
        current = current.children[pChunk]
      else:
        current = DirNode(pChunk, current)
        addCounter += 1

  #print addCounter

  return addCounter


def main(inputFilePath):
  cases = []
  try:
    inFile = open(inputFilePath, "r")

    try:
      caseCount = int(inFile.readline())
      for i in xrange(0,caseCount):
        rootNode = DirNode("/", None)
        casePaths = []
        startCount, newCount = inFile.readline().split()
        for j in xrange(0, int(startCount)):
          addPath(rootNode, inFile.readline())
        for j in xrange(0, int(newCount)):
          casePaths.append(inFile.readline())

        cases.append([casePaths, rootNode])

      inFile.close()

    finally:
      inFile.close()

  except IOError:
    print "Error reading from file!"

  for i in xrange(0, len(cases)):
    print "Case #%d: %d" % (i+1, caseResult(cases[i]))

def caseResult(case):
  counter = 0
  for i in xrange(0, len(case[0])):
    counter += addPath(case[1], case[0][i])

  return counter


if __name__ == "__main__":
  if(len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    print "Supply input file"


