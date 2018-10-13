def fill_board(board):
  R = len(board)
  C = len(board[0])
  all_blank = [True] * R
  left_ch = ["?"] * R
  for r in range(R):
    current_ch = "?"
    for c in range(C):
      if board[r][c] != "?":
        current_ch = board[r][c]
        all_blank[r] = False
        if left_ch[r] == "?":
          left_ch[r] = current_ch
      board[r][c] = current_ch
  # fill left
  for r in range(R):
    for c in range(C):
      if board[r][c] == left_ch[r]:
        break
      board[r][c] = left_ch[r]

  current_row = []
  first_non_blank = []
  for r in range(R):
    if not all_blank[r]:
      current_row = board[r][:]
      if not first_non_blank:
        first_non_blank = board[r][:]
      continue
    board[r] = current_row[:]

  for r in range(R):
    if not all_blank[r]:
      break
    board[r] = first_non_blank[:]

  for r in range(R):
    print("".join(board[r]))


num_tests = int(input().strip())
for test_id in range(1, num_tests + 1):
  R, C = map(int, input().strip().split())
  board = []
  for r in range(R):
    board.append(list(input().strip()))
  print("Case #{0}:".format(test_id))
  fill_board(board)