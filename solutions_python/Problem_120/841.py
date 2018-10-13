import sys
import math

class Solution(object):


  def runForCase(self, r, t):
    x = float(1-2*r)
    ret = x + math.sqrt(float(x*x+8*t))
    ret = ret / 4
    return int(ret)


  def runForTestCases(self, stream):
    testCases = int(stream.readline().strip())
    caseNumber = 1
    cases = []
    
    for _ in range(testCases):
      r, t = map(float, stream.readline().strip().split(" "))
      
      # print >> sys.stderr, caseNumber,
      print "Case #%s:" % caseNumber, self.runForCase(r, t)
      caseNumber += 1

if __name__ == "__main__":
  if len(sys.argv) == 2:
    _, filename = sys.argv
    Solution().runForTestCases(open(filename))