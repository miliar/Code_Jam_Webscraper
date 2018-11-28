

f = file('B-large.in')

cases = int(f.readline())


def solve(board, n, m):
  hor_max = [max(i) for i in board]
  ver_max = [max(i) for i in zip(*board[::-1])]
  for i in range(n):
    for j in range(m):
      if board[i][j] <  hor_max[i] and board[i][j] < ver_max[j]:
        return False 
  return True


for i in range(1, cases + 1):
  n, m = map(int, list(f.readline().split()))
  board = []
  for j in range(n):
    board.append(map(int, f.readline().split()))
  if solve(board, n, m):
    print 'Case #' + str(i) + ': YES' 
  else:
    print 'Case #' + str(i) + ': NO' 