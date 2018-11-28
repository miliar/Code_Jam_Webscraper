import re
f=open("A-large.in")
XWIN=re.compile("[XT]{4}")
OWIN=re.compile("[OT]{4}")
NF=re.compile("[.]")

hasEmpty = False
result = -1

outResult = ["X won","O won", "Draw","Game has not completed"]

def printResult(i, out):
  print "Case #"+str(i)+": "+out

def transpose(board):
  tboard = []
  for i in range(4):
    tboard.append(board[0][i]+board[1][i]+board[2][i]+board[3][i])
  return tboard

def cross(board):
  cross = []
  cross.append(board[0][0]+board[1][1]+board[2][2]+board[3][3])
  cross.append(board[0][3]+board[1][2]+board[2][1]+board[3][0])
  return cross
    
def checkRow(row):
  global hasEmpty, result
  if re.search(NF,row) is not None:
    hasEmpty = True
    return False
  if re.match(XWIN,row) is not None:
    result = 0
    return True
  if re.match(OWIN,row) is not None:
    result = 1
    return True
  return False

def solve(board):
  for row in board:
    if checkRow(row):
      return True
  return False

def solveAll(board):
  if solve(board):
    return True
  elif solve(transpose(board)):
    return True
  return solve(cross(board))

T = int(f.readline().rstrip())
for i in range(T):
  board=[]
  result=-1
  hasEmpty = False
  for j in range(4):
    board.append(f.readline().rstrip())

  if solveAll(board):
    pass
  elif hasEmpty: 
    result = 3 
  else:
    result = 2
  
  printResult(i+1, outResult[result])
  f.readline()

