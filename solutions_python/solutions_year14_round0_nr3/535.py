import numpy

def solve(rr, cc, m):
  board = numpy.array([['.'] * cc] * rr)
  diff = rr * cc - m
  r, c = min([rr,cc]), max([rr,cc])
  if diff is 1:
    board[:,:] = '*'
    board[0,0] = 'c'
    return print_board(board)
  if diff <= 0:
    return 'Impossible'
  if r is 1:
    if rr < cc:
      board[0,diff:] = '*'
    else:
      board[diff:,0] = '*'
    board[0,0] = 'c'
    return print_board(board)
  if diff < 4:
    return 'Impossible'
  if r is 2:
    if diff % 2 is 0:
      if rr < cc:
        board[:,diff / 2:] = '*'
      else:
        board[diff / 2:,:] = '*'
      board[0,0] = 'c'
      return print_board(board)
    else:
      return 'Impossible'
  if diff in [5,7]:
      return 'Impossible'
  else:
    board[:,:] = '*'
    if diff is 4:
      board[:2,:2] = '.'
    elif diff is 6:
      board[:3, :2] = '.'
    elif diff is 9:
      board[:3,:3] = '.'
    else:
      elim_cols, rem = divmod(diff, rr)
      if elim_cols is 1:
        if (rr - rem) % 2 is 0:
          board[:, :elim_cols +1] = '.'
          board[- (rr - rem) / 2:,:] = '*'
        else:
          board[:, :elim_cols +1] = '.'
          board[:3, elim_cols + 1] = '.'
          board[(rr - rem + 3) / 2:, :2] = '*'
      else:
        board[:, :elim_cols] = '.'
        if rem > 0:
          board[:rem, elim_cols] = '.'
        if rem is 1:
          board[1, elim_cols] = '.'
          board[-1, elim_cols - 1] = '*'
          if elim_cols is 2:
            board[2, elim_cols] = '.'
            board[-1,0] = '*'
    board[0,0] = 'c'
    return print_board(board)

def print_board(board):
  return '\n'.join([''.join(x) for x in list(board)])


np = int(raw_input())
for i in range(np):
  print 'Case #%i:\n%s' % (i + 1, solve(*map(int, raw_input().split(' '))))

