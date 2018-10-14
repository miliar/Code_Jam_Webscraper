import sys
import math

class FairSquare(object):

  def isFair(self, number):
    strNumber = str(number)
    return strNumber == strNumber[::-1]


  def runForCase(self, case):
    start, end = map(int, case)
    numbers = 0
    
    root = int(math.ceil(math.sqrt(start)))
    while True:
      if self.isFair(root):
        powNumber = pow(root, 2)
        if powNumber > end:
          break
        if self.isFair(powNumber):
          numbers += 1
      root += 1
    return str(numbers)



  def runForTestCases(self, stream):
    testCases = int(stream.readline().strip())
    caseNumber = 1
    for _ in range(testCases):
      start, end = map(int, stream.readline().strip().split(" "))
      case = (start, end)
      print "Case #%s:" % caseNumber, self.runForCase(case)
      caseNumber += 1

if __name__ == "__main__":
  if len(sys.argv) == 2:
    _, filename = sys.argv
    FairSquare().runForTestCases(open(filename))