import sys
rl = lambda : sys.stdin.readline().strip()

# 0 - win
# 1 - no win, has empty
# 2 - no win, no empty
def check(line, player):
  for i in line:
    if i != player and i != 'T':
      if '.' in line:
        return 1
      else:
        return 2
  return 0

# 1 - 'X'
# 2 - 'O'
# 3 - draw
# 4 - 'not completed'
def solve(board):
  has_empty = False

  for i in xrange(4):
    resX = check(board[i], 'X')
    if resX == 0:
      return 1
    resO = check(board[i], 'O')
    if resO == 0:
      return 2
    if resX == 1 or resO == 1:
      has_empty = True

  for i in xrange(4):
    cells = [board[0][i], board[1][i], board[2][i], board[3][i]]
    resX = check(cells, 'X')
    if resX == 0:
      return 1
    resO = check(cells, 'O')
    if resO == 0:
      return 2
    if resX == 1 or resO == 1:
      has_empty = True

  cells = [board[0][0], board[1][1], board[2][2], board[3][3]]
  resX = check(cells, 'X')
  if resX == 0:
    return 1
  resO = check(cells, 'O')
  if resO == 0:
    return 2
  if resX == 1 or resO == 1:
    has_empty = True

  cells = [board[0][3], board[1][2], board[2][1], board[3][0]]
  resX = check(cells, 'X')
  if resX == 0:
    return 1
  resO = check(cells, 'O')
  if resO == 0:
    return 2
  if resX == 1 or resO == 1:
    has_empty = True

  if has_empty:
    return 4
  else:
    return 3

def main():
  cases = int(rl())
  for c in xrange(1, cases+1):
    board = []
    for i in xrange(4):
      board.append(rl())
    res = solve(board)
    if res == 1:
      print "Case #%d: X won" % c
    elif res == 2:
      print "Case #%d: O won" % c
    elif res == 3:
      print "Case #%d: Draw" % c
    else:
      print "Case #%d: Game has not completed" % c
    rl()

main()
