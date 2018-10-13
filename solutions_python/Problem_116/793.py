

f = file('A-large.in')

def solve(board, player):
  t = ('T', player)
  for row in range(0, 4):
    if board[row][0] in t and board[row][1] in t and board[row][2] in t and board[row][3] in t:
      return True
  for col in range(0, 4):
    if board[0][col] in t and board[1][col] in t and board[2][col] in t and board[3][col] in t:
      return True
  for i in range(0, 4):
    if board[i][i] not in t:
      break
    if i == 3:
      return True
  for i in range(0, 4):
    if board[i][3 - i] not in t:
      break
    if i == 3:
      return True

  return False
  
def is_complete(board):
  for i in range(0, 4):
    for j in range(0, 4):
      if board[i][j] == '.':
        return False
  return True;

num = int(f.readline())

for i in range(0, num):
  board = []
  for j in range(0, 4):
    board.append(list(f.readline())[0:4])
  if solve(board, 'X'):
    print 'Case #' + str(i+1) + ': X won'
  elif solve(board, 'O'):
    print 'Case #' + str(i+1) + ': O won'
  elif is_complete(board):
    print 'Case #' + str(i+1) + ': Draw'
  else:
    print 'Case #' + str(i+1) + ': Game has not completed'
  f.readline()

  

