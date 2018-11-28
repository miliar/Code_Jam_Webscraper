for c in xrange(int(raw_input())):
  print "Case #"+str(c+1)+":",
  board = [raw_input() for i in xrange(4)]
  dots = False
  for i in xrange(4):
    xrow = True
    xcol = True
    orow = True
    ocol = True
    for j in xrange(4):
      dots = dots or board[i][j] == '.'
      xrow = xrow and (board[i][j] == 'X' or board[i][j] == 'T')
      xcol = xcol and (board[j][i] == 'X' or board[j][i] == 'T')
      orow = orow and (board[i][j] == 'O' or board[i][j] == 'T')
      ocol = ocol and (board[j][i] == 'O' or board[j][i] == 'T')
    if xrow or xcol:
      print "X won" 
      break
    elif orow or ocol:
      print "O won" 
      break
  else:
    xdiag1 = True
    xdiag2 = True
    odiag1 = True
    odiag2 = True
    for i in xrange(4):
      xdiag1 = xdiag1 and (board[i][i] == 'X' or board[i][i] == 'T')
      xdiag2 = xdiag2 and (board[i][3-i] == 'X' or board[i][3-i] == 'T')
      odiag1 = odiag1 and (board[i][i] == 'O' or board[i][i] == 'T')
      odiag2 = odiag2 and (board[i][3-i] == 'O' or board[i][3-i] == 'T')
    if xdiag1 or xdiag2:
      print "X won" 
    elif odiag1 or odiag2:
      print "O won" 
    elif dots:
      print "Game has not completed"
    else:
      print "Draw"
  empty = raw_input()
