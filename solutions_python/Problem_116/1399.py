import sys
import string
result = [
  "Game has not completed",
  "O won",
  "X won",
  "Draw",
]
def solution(input):
  board = []
  for line in input:
    board.append(map(int, list(line.strip())))
  result = board[0][0] & board[0][1] & board[0][2] & board[0][3] \
       or  board[1][0] & board[1][1] & board[1][2] & board[1][3] \
       or  board[2][0] & board[2][1] & board[2][2] & board[2][3] \
       or  board[3][0] & board[3][1] & board[3][2] & board[3][3] \
       or  board[0][0] & board[1][0] & board[2][0] & board[3][0] \
       or  board[0][1] & board[1][1] & board[2][1] & board[3][1] \
       or  board[0][2] & board[1][2] & board[2][2] & board[3][2] \
       or  board[0][3] & board[1][3] & board[2][3] & board[3][3] \
       or  board[0][0] & board[1][1] & board[2][2] & board[3][3] \
       or  board[0][3] & board[1][2] & board[2][1] & board[3][0]

  if result:
    return result

  if True in [0 in x for x in board]:
    return 0
      
  return 3

buf = sys.stdin.read()
lines = buf.translate(string.maketrans('.OXT', '0123')).splitlines()
T = int(lines[0])
lines = lines[1:]
for x in range(T):
  print "Case #%d: "%(x+1) + result[solution(lines[5 * x: 5 * x + 4])]
