import sys

def solve_board(board, i):
  for player in ['X','O']:
    for row in board:
      if (row.count(player) == 4 or  
        (row.count(player) == 3 and row.count('T') == 1)):
        print "Case #" + str(i + 1) + ": " + player + " won"
        return
    for col in range(0,4):
      col_text = ""
      for j in range(0,4):
        col_text += board[j][col]
      if (col_text.count(player) == 4 or  
        (col_text.count(player) == 3 and col_text.count('T') == 1)):
        print "Case #" + str(i + 1) + ": " + player + " won"
        return
    diag_1 = board[0][0] + board [1][1] + board[2][2] + board[3][3]
    if (diag_1.count(player) == 4 or  
      (diag_1.count(player) == 3 and diag_1.count('T') == 1)):
      print "Case #" + str(i + 1) + ": " + player + " won"
      return
    diag_2 = board[0][3] + board [1][2] + board[2][1] + board[3][0]
    if (diag_2.count(player) == 4 or  
      (diag_2.count(player) == 3 and diag_2.count('T') == 1)):
      print "Case #" + str(i + 1) + ": " + player + " won"
      return
  period_count = 0
  for row in board:
    period_count += row.count('.')
  if period_count == 0:
    print "Case #" + str(i + 1) + ": Draw"
  else:
    print "Case #" + str(i + 1) + ": Game has not completed"  

num_problems = int(sys.stdin.readline())
for i in range(0,num_problems):
  board = []
  for j in range(0,4):
    row = sys.stdin.readline()[0:4]
    board.append(row)
  solve_board(board, i)
  sys.stdin.readline()


