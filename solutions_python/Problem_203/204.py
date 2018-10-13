def GetCake(board):
  """Returns a list of strings, each string represents the completed board.
  """
  nrow, ncol = len(board), len(board[0])
  row_filled = [False] * nrow
  def FillRow(myrow):
    """Returns the filed row, together with whether the board has been changed.
    """
    row = list(myrow)
    curr = '?'
    N = len(row)
    first_letter = '?'
    first_letter_idx = -1
    for i in range(N):
      if row[i] == '?':
        row[i] = curr
      else:
        curr = row[i]
        if first_letter == '?':
          first_letter = curr
          first_letter_idx = i
    if first_letter != '?':
      for i in range(first_letter_idx):
        row[i] = first_letter
    return ''.join(row), first_letter != '?'
  filled_board = [board[row] for row in range(nrow)]
  for r in range(nrow):
    # Check if current row contains any cake
    myrow = board[r]
    filled_board[r], row_filled[r] = FillRow(myrow)
  # Fill all rows using the same strategy
  curr = '?' * ncol
  first_row_idx = row_filled.index(True)
  for i in range(nrow):
    if row_filled[i]:
      curr = filled_board[i]
    else:
      filled_board[i] = curr
  for i in range(first_row_idx):
    filled_board[i] = filled_board[first_row_idx]
  return filled_board

if __name__ == '__main__':
  T = int(input())
  for i in range(1, T + 1):
    R, C = map(int, input().split())
    board = []
    for r in range(R):
      board.append(input())
    output = GetCake(board)
    print('Case #{}:'.format(i))
    for row in output:
      print(row)
