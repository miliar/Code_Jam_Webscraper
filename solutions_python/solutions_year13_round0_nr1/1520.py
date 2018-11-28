
def checkRow(board, row, symbol):
  # Check for win
  for i in range(4):
    if board[row][i] != symbol and board[row][i] != 'T':
      return False
  return True
    
def checkCol(board, col, symbol):
  # Check for win
  for i in range(4):
    if board[i][col] != symbol and board[i][col] != 'T':
      return False
  return True

def checkDiag1(board, symbol):
  # Check for win
  for i in range(4):
    if board[i][i] != symbol and board[i][i] != 'T':
      return False
  return True

def checkDiag2(board, symbol):
  # Check for win
  for i in range(4):
    j = 3 - i
    if board[i][j] != symbol and board[i][j] != 'T':
      return False
  return True


def wins(board, symbol):
  # Rows
  for i in range(4):
    if checkRow(board, i, symbol):
      return True
  # Cols
  for i in range(4):
    if checkCol(board, i, symbol):
      return True
  # Diag1
  if checkDiag1(board, symbol):
    return True
  # Diag2
  if checkDiag2(board, symbol):
    return True
  return False

def containsdot(board):
  for row in board:
    for char in row:
      if char == '.':
        return True
  return False


with open('A.in', 'r') as fin:
  with open('A.out', 'w') as fout:
    lines = fin.readlines()
    lidx = 0
    T = int(lines[lidx])
    lidx += 1
    for case in range(T):
      # Read in the board
      board = []
      for i in range(4):
        board.append(list(lines[lidx+i].strip()))
      lidx += 5

      if wins(board, 'X'):
        fout.write('Case #%s: X won\n' % (case+1))
      elif wins(board, 'O'):
        fout.write('Case #%s: O won\n' % (case+1))
      elif containsdot(board):
        fout.write('Case #%s: Game has not completed\n' % (case+1))
      else:
        fout.write('Case #%s: Draw\n' % (case+1))

      print board
      
