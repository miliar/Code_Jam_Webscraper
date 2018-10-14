# Solver for Tic-Tac-Toe-Tomek game
import numpy as np

fin = open('A-large.in')
fout = open('testout_large.txt', 'w')

def CheckWinner(A, player_char, not_player_char):
  # Check if X wins
  Acopy = A
  Acopy = np.where(Acopy=='.', 0, Acopy)
  Acopy = np.where(Acopy==not_player_char,0,Acopy)
  Acopy = np.where(Acopy=='T',1,Acopy)
  Acopy = np.where(Acopy==player_char,1,Acopy)
  Acopy = np.array(Acopy, dtype=int)
  # print(Acopy)
  if max(np.sum(Acopy,0))==4 or max(np.sum(Acopy,1))==4 or np.trace(Acopy)==4 or sum(Acopy[[0,1,2,3], [3,2,1,0]])==4:
    return(True)
  else:
    return(False)
  

T = int(fin.readline().rstrip('\n'))
for j in range(1,T+1,1):
  board = []
  line = fin.readline()
  while line != '\n' and line != '':
    board.append(list(line.strip('\n')))
    line = fin.readline()
  # CheckWinner(array)
  # print(board)
  matboard = np.array(board)
  if CheckWinner(matboard, 'X', 'O'):
    fout.write('Case #%d: X won\n' %j)
  elif CheckWinner(matboard, 'O', 'X'):
    fout.write('Case #%d: O won\n' %j)
  elif np.in1d(['.'], matboard).all():
    fout.write('Case #%d: Game has not completed\n' %j)
  else:
    fout.write('Case #%d: Draw\n' %j)
  

fin.close()
fout.close()