def hor(board, val):
  for j in xrange(4):
    for i in xrange(4):
      if val == board[j][i] or board[j][i] == "T":
        if i == 3:
          return True
      else:
        break
  return False

def vert(board, val):
  for i in xrange(4):
    for j in xrange(4):
      if val == board[j][i] or board[j][i] == "T":
        if j == 3:
          return True
      else:
        break
  return False

def diag(board, val):
  if (board[0][0] == val or board[0][0] == "T") and (board[1][1] == val or board[1][1] == "T") and (board[2][2] == val or board[2][2] == "T") and (board[3][3] == val or board[3][3] == "T"):
    return True
  if (board[0][3] == val or board[0][3] == "T") and (board[1][2] == val or board[1][2] == "T") and (board[2][1] == val or board[2][1] == "T") and (board[3][0] == val or board[3][0] == "T"):
    return True
  return False

def done(board):
  for line in board:
    for letter in line:
      if letter == ".":
        return False
  return True
      

times = int(raw_input())
for time in xrange(times):
  board = []
  for i in xrange(4):
    board.append(raw_input())
  throwaway = raw_input()
  


  xwon = hor(board,"X") or vert(board,"X") or diag(board,"X")
  owon = hor(board,"O") or vert(board,"O") or diag(board,"O")
  d = done(board)
  message = ""
  if xwon and not owon:
    message = "X won"
  elif not xwon and owon:
    message = "O won"
  elif not xwon and not owon and not d:
    message = "Game has not completed"
  else:
    message = "Draw"
  print "Case #%d: %s" % (time+1, message)

