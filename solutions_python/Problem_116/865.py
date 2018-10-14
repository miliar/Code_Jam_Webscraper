import sys

def single(line):
  x_count = line.count("X")
  o_count = line.count("O")
  dot_count = line.count(".")
  T_count = line.count("T")
  if x_count == 4 or (x_count == 3 and T_count == 1):
    return "X"
  if o_count == 4 or (o_count == 3 and T_count == 1):
    return "O"
  if dot_count:
    return "G"
  return "D"

def judge(board):
  incomplete = 0
  for row in xrange(4):
    result = single(board[row])
    if result == "X" or result == "O":
      return result + " won"
    elif result == "G":
      incomplete += 1
  for col in xrange(4):
    line = ""
    for row in xrange(4):
      line += board[row][col]
    result = single(line)
    if result == "X" or result == "O":
      return result + " won"
    elif result == "G":
      incomplete += 1
  diag = ""
  diag2 = ""
  for ind in xrange(4):
    diag += board[ind][ind]
    diag2 += board[3-ind][ind]
  result1 = single(diag)
  if result1 == "X" or result1 == "O":
    return result1 + " won"
  elif result1 == "G":
    incomplete += 1
  result2 = single(diag2)
  if result2 == "X" or result2 == "O":
    return result2 + " won"
  elif result2 == "G":
    incomplete += 1
  if incomplete:
    return "Game has not completed"
  else:
    return "Draw"


readline = sys.stdin.readline
T = int(readline())
for t in xrange(T):
  first = readline()
  board = []
  if first == "\n":
    board = [readline()]
  else:
    board = [first]
  for x in xrange(0,3):
    board.append(readline())
  print "Case #%d: " % (t+1) + judge(board)


