import sys

class TicTacToe(object):


  def makeColRowArray(self, case):
    colRowCase = []
    for col in range(4):
      colRowCase.append("".join([case[r][col] for r in range(4)]))
    return colRowCase

  def checkWon(self, line):
    oSymbols = line.count("O") + line.count("T") 
    xSymbols = line.count("X") + line.count("T")
    if oSymbols == 4:
      return "O won"
    if xSymbols == 4:
      return "X won"
    return None

  def checkForCase(self, case):
    colRowCase = self.makeColRowArray(case)
    # Check win
    for row in range(4):
      won = self.checkWon(case[row])
      if won:
        return won

    for col in range(4):
      won = self.checkWon(colRowCase[col])
      if won:
        return won
    # Diag
    diag1 = "".join([case[i][i] for i in range(4)])
    diag2 = "".join([case[i][3-i] for i in range(4)])
    for diag in [diag1, diag2]:
      won = self.checkWon(diag)
      if won:
        return won
    # Check draw
    if "." not in "".join(case):
      return "Draw"
    else:
      return "Game has not completed"

  def runForTestCases(self, stream):
    testCases = stream.readline()
    case = []
    caseNumber = 1
    for line in stream.xreadlines():
      line = line.strip()
      if not line:
        continue
      case.append(line)
      if len(case) == 4:
        print "Case #%s:" % caseNumber, self.checkForCase(case)
        caseNumber += 1
        case = []

if __name__ == "__main__":
  if len(sys.argv) == 2:
    _, filename = sys.argv
    TicTacToe().runForTestCases(open(filename))