import math, re, sys

def isWinner(row):
  match = re.search('[TX]{4}',row)
  if match:
    return [True,"X"]
  match = re.search('[TO]{4}',row)
  if match:
    return [True,"O"]
  return [False]

def findWinner(board):
  gameDefinitelyFinished = True
  for row in board:
    for column in row:
      if column == '.':
        gameDefinitelyFinished = False 
    winner = isWinner(row[0]+row[1]+row[2]+row[3])
    if winner[0]:
      return winner[1] + " won"
  for columnNum,column in enumerate(board[0]):
    winner = isWinner(board[0][columnNum]+board[1][columnNum]+board[2][columnNum]+board[3][columnNum])
    if winner[0]:
      return winner[1] + " won"
  winner = isWinner(board[0][0]+board[1][1]+board[2][2]+board[3][3])
  if winner[0]:
    return winner[1] + " won"
  winner = isWinner(board[0][3]+board[1][2]+board[2][1]+board[3][0])
  if winner[0]:
    return winner[1] + " won"
  if gameDefinitelyFinished:
    return "Draw"
  else:
    return "Game has not completed"

cases = 0
board = []

for count,line in enumerate(sys.stdin):
  if count == 0:
    cases = int(line)
    continue

  if count % 5 == 0:
    continue

  boardRow = [line[0:1],line[1:2],line[2:3],line[3:4]]
  board.append(boardRow)

  if count % 5 == 4:
    print "Case #" + str(int(math.floor(count/5)) + 1) + ": " + findWinner(board)
    board = []  

  if count == cases*5:
    break

