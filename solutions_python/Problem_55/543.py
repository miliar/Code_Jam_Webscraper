"""To use pass the path of the input file as the only argument"""

import sys

def main(inputFilePath):
  """Main Method for parsing file and starting calculation exec"""
  cases = []
  try:
    inFile = open(inputFilePath, "r")

    try:
      caseCount = int(inFile.readline())
      for i in xrange(0, caseCount):
        case = inFile.readline().split()
        case.append(inFile.readline().split())
        cases.append(case)

      inFile.close()

    finally:
      inFile.close()

  except IOError:
    print "Error reading from file!"

  for i in xrange(0, len(cases)):
    print "Case #%d: %d" % (i+1, calculateRevenue(cases[i]))

class myQueue:
  """Simple Queue implementation with constant time Offer and Poll"""
  class QueueNode:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.__head = None
    self.__tail = None

  def offer(self, value):
    newTail = myQueue.QueueNode(value)
    if(self.__head == None):
      self.__head = newTail
    if(self.__tail != None):
      self.__tail.next = newTail

    self.__tail = newTail

  def peek(self):
    return self.__head.value

  def poll(self):
    oldHead = self.__head
    if(self.__tail == oldHead):
      self.__tail = None
    if(self.__head != None):
      self.__head = oldHead.next
    
    return oldHead.value

  def empty(self):
    return self.__head == None

def calculateRevenue(case):
  """Given a case (a list of 4 elements) return the number of sales
    Case: [Runs, Capacity, GroupNo, [Groups]]
  """

  runs      = int(case[0])
  capacity  = int(case[1])
  groups    = case[3]
  line = myQueue()
  revenue = 0

  for group in groups:
    line.offer(int(group))

  for run in xrange(0, runs):
    remain = capacity
    runSet = []
    while(not line.empty()):
      if(line.peek() > remain):
        break;

      nextGroup = line.poll()
      runSet.append(nextGroup)
      remain    -= nextGroup
      revenue   += nextGroup

    for group in runSet:
      line.offer(group)

  return revenue
      

if __name__ == "__main__":
  if(len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    print "Must give input file"
