def check_line(board, line):
  ctx = 0
  cto = 0
  for i in range(4):
    if board[line][i] == 'X':
      ctx = ctx + 1
    elif board[line][i] == 'O':
      cto = cto + 1
    elif board[line][i] == 'T':
      ctx = ctx + 1
      cto = cto + 1
    else:
      return 'Game has not completed'
  
  if ctx == 4:
    return 'X won'
  elif cto == 4:
    return 'O won'
  else:
    return 'filled'
    
def check_col(board, col):
  ctx = 0
  cto = 0
  for i in range(4):
    if board[i][col] == 'X':
      ctx = ctx + 1
    elif board[i][col] == 'O':
      cto = cto + 1
    elif board[i][col] == 'T':
      ctx = ctx + 1
      cto = cto + 1
    else:
      return 'Game has not completed'
  
  if ctx == 4:
    return 'X won'
  elif cto == 4:
    return 'O won'
  else:
    return 'filled'

def check_diag(board, diag):
  ctx = 0
  cto = 0
  if diag == 0:
    op = [3,2,1,0]
  else:
    op = [0,1,2,3]
  for i in range(4):
    if board[op[i]][i] == 'X':
      ctx = ctx + 1
    elif board[op[i]][i] == 'O':
      cto = cto + 1
    elif board[op[i]][i] == 'T':
      ctx = ctx + 1
      cto = cto + 1
    else:
      return 'Game has not completed'
  
  if ctx == 4:
    return 'X won'
  elif cto == 4:
    return 'O won'
  else:
    return 'filled'

def check_board(board):
  cur = 'filled'
  for ck in range(4):
    v = check_line(board, ck)
    if v != 'filled' and v != 'Game has not completed':
      return v
    if v != 'filled':
      cur = v
    v = check_col(board, ck)
    if v != 'filled' and v != 'Game has not completed':
      return v
    if v != 'filled':
      cur = v
  for dg in range(2):
    v = check_diag(board, dg)
    if v != 'filled' and v != 'Game has not completed':
      return v
    if v != 'filled':
      cur = v
  if v == 'filled':
    return 'Draw'
  else:
    return v

T = int(raw_input())
  
for case in range(1,T+1):
  board = 4*['']
  for i in range(4):
    board[i] = raw_input()
  try:
    empty_line = raw_input()
  except:
    pass
  print 'Case #' + str(case) + ': ' + check_board(board) 