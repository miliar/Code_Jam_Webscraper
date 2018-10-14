# Google Code Jam 2013
# Problem A. Tic-Tac-Toe-Tomek

cases = int(raw_input())

def won(p, b):
  r = False

  for i in range(4):
    count = 0
    for j in range(4):
      if b[i][j] == p or b[i][j] == 'T':
        count += 1
    if count == 4:
      r = True

  for i in range(4):
    count = 0
    for j in range(4):
      if b[j][i] == p or b[j][i] == 'T':
        count += 1
    if count == 4:
      r = True

  count = 0

  for i in range(4):
    if b[i][i] == p or b[i][i] == 'T':
      count += 1

  if count == 4:
    r = True

  count = 0

  for i in range(4):
    if b[3-i][i] == p or b[3-i][i] == 'T':
      count += 1

  if count == 4:
    r = True

  return r



def full(b):
  for i in range(4):
    for j in range(4):
      if b[i][j] == '.':
        return False
  
  return True


for cases_r in range(cases):

  board = []
  for i in range(4):
    board.append(raw_input())

  players = ['X', 'O']

  result = False

  for p in players:
    if not result and won(p, board):
      result = True
      sol = "%s won" %(p)

  if not result and full(board):
    result = True
    sol = "Draw"

  if not result:
    sol = "Game has not completed"

  print "Case #%d: %s" %(cases_r+1, sol)

  raw_input()

