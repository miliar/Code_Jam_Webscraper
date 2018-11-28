def checkBoard():

  # Check rows
  for i in range(4):
    countX = 0
    countO = 0
    countT = 0
    for j in range(4):
      if (board[i][j]=='X'): countX += 1
      elif (board[i][j]=='O'): countO += 1
      elif (board[i][j]=='T'): countT += 1
    if (countX==4 or (countX==3 and countT==1)): return "X won"
    elif (countO==4 or (countO==3 and countT==1)): return "O won"
    
  # Check columns
  for j in range(4):
    countX = 0
    countO = 0
    countT = 0
    for i in range(4):
      if (board[i][j]=='X'): countX += 1
      elif (board[i][j]=='O'): countO += 1
      elif (board[i][j]=='T'): countT += 1
    if (countX==4 or (countX==3 and countT==1)): return "X won"
    elif (countO==4 or (countO==3 and countT==1)): return "O won"

  # Check diagonals
  countX = 0
  countO = 0
  countT = 0
  for i in range(4):
    if (board[i][i]=='X'): countX += 1
    elif (board[i][i]=='O'): countO += 1
    elif (board[i][i]=='T'): countT += 1
  if (countX==4 or (countX==3 and countT==1)): return "X won"
  elif (countO==4 or (countO==3 and countT==1)): return "O won"

  countX = 0
  countO = 0
  countT = 0
  for i in range(4):
    if (board[3-i][i]=='X'): countX += 1
    elif (board[3-i][i]=='O'): countO += 1
    elif (board[3-i][i]=='T'): countT += 1
  if (countX==4 or (countX==3 and countT==1)): return "X won"
  elif (countO==4 or (countO==3 and countT==1)): return "O won"
    
  # If no winner, determine tie or game not completed
  # Check for at least one dot
  for i in range(4):
    for j in range(4):
      if (board[i][j]=='.'): return "Game has not completed"
  return "Draw"

f = open("A-large.in","r")
numTestCases = int(f.readline())

for testNum in range(numTestCases):
  
  # Read test case and load into matrix
  board = [['','','',''],['','','',''],['','','',''],['','','','']]
  for i in range(4):
    data = f.readline().strip()
    for j in range(4):
      board[i][j] = data[j]

  # Check board and print status
  result = checkBoard()
  print "Case #%i: %s" % (testNum+1, result)
  
  f.readline()

f.close()

