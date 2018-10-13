import re

x_regex = [
"[XT][XT][XT][XT]",
"[XT]...[XT]...[XT]...[XT]",
"[XT]....[XT]....[XT]....[XT]",
"[XT].....[XT].....[XT].....[XT]"
]

o_regex = [
"[OT][OT][OT][OT]",
"[OT]...[OT]...[OT]...[OT]",
"[OT]....[OT]....[OT]....[OT]",
"[OT].....[OT].....[OT].....[OT]"
]

def check_win(board, regex):
  for r in regex:
    if re.search(r, board, re.DOTALL) is not None:
      return True
  return False

def x_win(board):
  return check_win(board, x_regex)

def o_win(board):
  return check_win(board, o_regex)

#####
f = open("data")
o = open("out", 'w')
cases = int(f.readline())

for i in range(cases):
  # Read the board
  board = f.readline() + f.readline() + f.readline() + f.readline()
  f.readline() # Trailing newline

  if x_win(board):
    result = "X won"

  elif o_win(board):
    result = "O won"

  elif '.' not in board:
    result = "Draw"

  else:
    result = "Game has not completed"


  o.write("Case #%d: %s\n" % (i+1, result))
