
f = open('A-large.in')
numInputs = int(f.readline())

cases = range(numInputs)
caseNumber = 0

xwon = "X won"
owon = "O won"

def getColumn(board, column):
  el0 = board[0][column]
  el1 = board[1][column]
  el2 = board[2][column]
  el3 = board[3][column]
  return [el0, el1, el2, el3]

def getDiagonal(board, num):
  if num == 0:
    el0 = board[0][0]
    el1 = board[1][1]
    el2 = board[2][2]
    el3 = board[3][3]
    return [el0, el1, el2, el3]
  if num == 1:
    el0 = board[3][0]
    el1 = board[2][1]
    el2 = board[1][2]
    el3 = board[0][3]
    return [el0, el1, el2, el3]



def checkFull(board):
  for i in range(4):
    if board[i].count('.') > 0:
      return False
  return True

def parseVector(vector):

  if vector.count('X') == 4 or (vector.count('X') == 3 and vector.count('T') == 1):
    cases[caseNumber] = xwon
    return True
  if vector.count('O') == 4 or (vector.count('O') == 3 and vector.count('T') == 1):
    cases[caseNumber] = owon
    return True

  return False


def solveBoard(board):

  for i in range(4):
    if parseVector(board[i]):
      return

  for i in range(4):
    if parseVector(getColumn(board, i)):
      return

  for i in range(2):
    if parseVector(getDiagonal(board, i)):
      return

  if checkFull(board):
    cases[caseNumber] = "Draw"
  else:
    cases[caseNumber] = "Game has not completed"


#print "Parsing {0} lines".format(numInputs)

for i in range(numInputs):
  row1 = list(f.readline())
  row2 = list(f.readline())
  row3 = list(f.readline())
  row4 = list(f.readline())

  board = [row1, row2, row3, row4]
  

  solveBoard(board)
  caseNumber += 1
  

  # Read the empty line
  f.readline()


for i,case in enumerate(cases):
  print 'Case #{0}: {1}'.format(i+1, case)

