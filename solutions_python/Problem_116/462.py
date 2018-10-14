import sys

def out(i, s):
  print
  sys.exit()

n = int(sys.stdin.readline())
for i in range(n):
  board = [];
  for l in range(4):
    board.append(sys.stdin.readline().strip());
  sys.stdin.readline()
  someoneWon = False
  for p in ['X', 'O']:
    for k in range(4):
      winV = True
      winH = True
      for t in range(4):
        if not board[k][t] in [p, 'T']:
          winH = False
        if not board[t][k] in [p, 'T']:
          winV = False
      if winV or winH:
        break
    winD = (board[0][0] in [p, 'T'] and board[1][1] in [p, 'T'] and board[2][2] in [p, 'T'] and \
           board[3][3] in [p, 'T']) or (board[3][0] in [p, 'T'] and board[2][1] in [p, 'T'] and \
           board[1][2] in [p, 'T'] and board[0][3] in [p, 'T']);
    if winV or winH or winD:
      print "Case #" + str(i+1) + ": " + p + " won"
      someoneWon = True
      break
      
  if someoneWon:
    continue
  
  finished = True
  for l in range(4):
    for k in range(4):
      if board[l][k] == '.':
        finished = False
  
  if finished:
    print "Case #" + str(i+1) + ": Draw"
  else:
    print "Case #" + str(i+1) + ": Game has not completed"