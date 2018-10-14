def solve(board):
  players = ["X", "O"]
  joker = "T"
  draw = True
  for player in players:
    won_diag1 = True
    won_diag2 = True
    for i in range(4):
      won_row = True
      won_col = True
      for j in range(4):
        if board[i][j] == ".":
          draw = False
        if board[i][j] not in [player, joker]:
          won_row = False
        if board[j][i] not in [player, joker]:
          won_col = False
      if board[i][i] not in [player, joker]:
        won_diag1 = False
      if board[i][3 - i] not in [player, joker]:
        won_diag2 = False
      if won_row or won_col:
        return "%s won" % player
    if won_diag1 or won_diag2:
      return "%s won" % player
  if draw:
    return "Draw"
  else:
    return "Game has not completed"

def main():
  T = int(input())
  for case in range(1, T + 1):
    board = [input() for i in range(4)]
    print("Case #%d: %s" % (case, solve(board)))
    input()

if __name__ == "__main__":
  main()
