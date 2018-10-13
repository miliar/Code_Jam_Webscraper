import sys

inputFile = sys.stdin
count = int(inputFile.readline())

def check(board, k, c, x, y, xd, yd):
  for i in xrange(k) :
    if x < 0 or x >= len(board):
      return False
    if y < 0 or y >= len(board):
      return False
    try :
      if board[x][y] != c:
        return False
    except:
      return False
    x += xd
    y += yd

  return True

def won(board, k, c):
  for x in xrange(len(board)):
    for y in xrange(len(board)):
      for xd in (-1, 0, 1):
        for yd in (-1, 0, 1):
          if xd == yd == 0:
            continue
          if check(board, k, c, x, y, xd, yd):
            return True
  return False

def gravity(board):
  for col in xrange(len(board)-1, -1, -1):
    for row in xrange(len(board)-1, -1, -1):
      # print row, col, board[row][col]
      if board[row][col] == '.':
        for d in xrange(len(board)):
          if row-d < 0:
            break
          if board[row-d][col] != '.':
            board[row][col] = board[row-d][col]
            board[row-d][col] = '.'
            break
  return board
      

def rotate(board):
  b = zip(*board[::-1])
  l = []
  for r in b:
    l.append(list(r))
  return l

def p(board):
  for r in board:
    print ''.join(r)
  print

for lineno in xrange(1, count+1):
  N, K = map(int, inputFile.readline().split())

  board = []
  for n in xrange(N):
    board.append(inputFile.readline().strip())

  left = gravity(rotate(board))
  """
  print K
  p(board)
  p(left)
  """

  r = won(left, K, 'R')
  b = won(left, K, 'B')

  print "Case #%d:" % lineno, 
  if r and b:
    print "Both"
  elif r:
    print "Red"
  elif b:
    print "Blue"
  else:
    print "Neither"

  lineno += 1
