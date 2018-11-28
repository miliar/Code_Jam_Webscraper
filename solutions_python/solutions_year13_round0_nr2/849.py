import sys

class Lawnmower(object):

  def noHigherGrassInCol(self, case, col, height):
    for rowHeights in case:
      h = rowHeights[col]
      if h > height:
        return False
    return True

  def noHigherGrassInRow(self, case, row, height):
    for h in case[row]:
      if h > height:
        return False
    return True

  def checkForCase(self, case, width, length):
    # Check win
    for row in range(width):
      for col in range(length):
        if not self.noHigherGrassInRow(case, row, case[row][col]) and not self.noHigherGrassInCol(case, col, case[row][col]):
          return "NO"
    return "YES"


  def runForTestCases(self, stream):
    testCases = int(stream.readline().strip())
    caseNumber = 1
    for _ in range(testCases):
      width, length = map(int, stream.readline().strip().split(" "))
      case = []
      for _ in range(width):
        case.append(map(int, stream.readline().strip().split(" ")))
      print "Case #%s:" % caseNumber, self.checkForCase(case, width, length)
      caseNumber += 1

if __name__ == "__main__":
  if len(sys.argv) == 2:
    _, filename = sys.argv
    Lawnmower().runForTestCases(open(filename))