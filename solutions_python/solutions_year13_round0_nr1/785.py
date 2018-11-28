def solve(n):
  board = [list(raw_input()) for i in xrange(4)]
  def check_rows(letter):
    return any( all( e == letter or e == 'T' for e in row) for row in board)
  def check_columns(letter):
    return any( all( e == letter or e == 'T' for e in col) for col in zip(*board[::-1]))
  def check_diagonals(letter):
    return all( board[i][i] == letter or board[i][i] == 'T' for i in xrange(4)) or \
      all(board[3-i][i] == letter or board[3-i][i] == 'T' for i in xrange(4))
  #check row
  start = "Case #{}: ".format(n)
  if check_rows('X') or check_columns('X') or check_diagonals('X'):
    print start + "X won"
  elif check_rows('O') or check_columns('O') or check_diagonals('O'):
    print start + "O won"
  elif any( any( e == '.' for e in row) for row in board):
    print start + "Game has not completed"
  else:
    print start + "Draw"

n = int(raw_input())
for i in xrange(n):
  solve(i+1)
  if i+1 < n:
    raw_input() #blank lines
  