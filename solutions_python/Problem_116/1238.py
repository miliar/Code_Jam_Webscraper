lines = [l[:-1] for l in open("biginput")][1:]

def find_winner(board):
  number_of_dots = 0
  dx = [-1, -1, -1, 0,  0,  1, 1, 1]
  dy = [-1,  0,  1, 1, -1, -1, 0, 1]

  for row in range(4):
    for col in range(4):
      if board[row][col] == ".":
        number_of_dots += 1
        continue

      want = board[row][col]

      for DIR in range(8):
        found = True

        for dist in range(4):
          new_x = row + dx[DIR] * dist
          new_y = col + dy[DIR] * dist
          
          if new_x < 0 or new_x > 3 or new_y < 0 or new_y > 3 or (board[new_x][new_y] != want and board[new_x][new_y] != 'T'):
            found = False
            break

        if found: return want + " won" 

  if number_of_dots == 0: return "Draw"

  return 'Game has not completed'

case = 0
while len(lines) > 0:
  case += 1
  board = []

  for x in range(4):
    board.append(lines.pop(0))
  lines.pop(0)

  winner = find_winner(board)
  print "Case #%d: %s" % (case, winner)

