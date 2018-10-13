# tomek.py
import sys

def solve_board(board):
  complete = True
  for line in board:
    if complete and '.' in line: complete = False
    if line.upper().replace('T','X') == 'XXXX': return "X won"
    elif line.upper().replace('T','O') == 'OOOO': return "O won"
  for i in range(4):
    if str(board[0][i]+board[1][i]+board[2][i]+board[3][i]).upper().replace('T','X') == 'XXXX': return "X won"
    if str(board[0][i]+board[1][i]+board[2][i]+board[3][i]).upper().replace('T','O') == 'OOOO': return "O won"
  if str(board[0][0]+board[1][1]+board[2][2]+board[3][3]).upper().replace('T','X') == 'XXXX': return "X won"
  if str(board[0][0]+board[1][1]+board[2][2]+board[3][3]).upper().replace('T','O') == 'OOOO': return "O won"
  if str(board[0][3]+board[1][2]+board[2][1]+board[3][0]).upper().replace('T','X') == 'XXXX': return "X won"
  if str(board[0][3]+board[1][2]+board[2][1]+board[3][0]).upper().replace('T','O') == 'OOOO': return "O won"
  if complete: return "Draw"
  return "Game has not completed"

if __name__ == '__main__':
  n = int(sys.stdin.readline())

  curr_board = None

  i = 1
  for line in sys.stdin:
    if line.strip() != '':
      if not curr_board: curr_board = []
      curr_board.append(line.strip())
    else: 
      print "Case #" + str(i) + ": " + str(solve_board(curr_board))
      curr_board = None
      i+=1
      
  if curr_board: print "Case #" + str(i) + ": " + str(solve_board(curr_board)) # solve the last board if needed

