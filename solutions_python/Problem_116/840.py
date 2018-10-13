def solve(board):
  dot = 0
  for i in range(4):
    X = 0
    O = 0
    for j in range(4):
      if board[i][j] == 'X':
        X = X +1
      elif board[i][j] == 'O':
        O = O +1
      elif board[i][j] == 'T':
        X = X +1
        O = O +1
      elif board[i][j] == '.':
        dot = 1
    if X == 4:
      return "X won"
    elif O == 4:
      return "O won"

  for i in range(4):
    X = 0
    O = 0
    for j in range(4):
      if board[j][i] == 'X':
        X = X +1
      elif board[j][i] == 'O':
        O = O +1
      elif board[j][i] == 'T':
        X = X +1
        O = O +1
    if X == 4:
      return "X won"
    elif O == 4:
      return "O won"

  X = 0
  O = 0
  for j in range(4):
    if board[j][j] == 'X':
      X = X +1
    elif board[j][j] == 'O':
      O = O +1
    elif board[j][j] == 'T':
      X = X +1
      O = O +1
  if X == 4:
    return "X won"
  elif O == 4:
    return "O won"

  X = 0
  O = 0
  for j in range(4):
    if board[j][3 - j] == 'X':
      X = X +1
    elif board[j][3 - j] == 'O':
      O = O +1
    elif board[j][3 - j] == 'T':
      X = X +1
      O = O +1
  if X == 4:
    return "X won"
  elif O == 4:
    return "O won"

  if dot == 0:
    return "Draw"
  else:
    return "Game has not completed"

    


File = open("A-large.in", "r")
f = []
for line in File:
  f.append(line)
for i in range(int(f[0])):
  print "Case #%d:" %(i+1), solve(f[i * 5 + 1 : i * 5 + 5])