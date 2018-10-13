import sys

text = {'X' : 'X won', 'd': 'Draw', 'O' : 'O won', 'n' : 'Game has not completed'}

def getWinner(board):
  empty = False
  #horizontal
  for i in range(4):
    current = board[i][0]
    if current == 'T':
      current = board[i][1]
    won = True
    for y in range(4):
      if board[i][y] == '.':
        empty = True
      if not (board[i][y] == current or board[i][y] == 'T'):
        won = False
    if won and current != '.':
      return current
      
  #vertical
  for i in range(4):
    current = board[0][i]
    if current == 'T':
      current = board[1][i]
    won = True
    for y in range(4):
      if board[y][i] == '.':
        empty = True
      if not (board[y][i] == current or board[y][i] == 'T'):
        won = False
    if won and current != '.':
      return current
  #diagonal
  won = True
  current = board[0][0]
  if current == 'T':
    current = board[1][1]
  if current != '.':
    for i in range(4):
      if not (board[i][i] == current or board[i][i] == 'T'):
        won = False
        break
    if won:
      return current

  #other diagonal
  won = True
  current = board[0][3]
  if current == 'T':
    current = board[1][2]
  if current != '.':
    for i in range(4):
      if not (board[i][3-i] == current or board[i][3-i] == 'T'):
        won = False
        break
    if won:
      return current
  if empty:
    return 'n'
  return 'd'

if __name__=="__main__":
  lines = sys.stdin.readlines()
  i = 1
  case = 1
  while i < len(lines):
    board = [line.strip() for line in lines[i:i+4]]
    winner = getWinner(board)
    print "Case #{}: {}".format(case, text[winner])
    case += 1
    i += 5
