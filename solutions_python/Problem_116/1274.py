#!/usr/bin/python2 -tt

import sys

def solve(board): 
  out = ""
  
  board1 = list(board)
  board2 = list(board)
  for i in range(4): 
    board1[i] = board1[i].replace('T', 'X')
    board2[i] = board2[i].replace('T', 'O')

  completed = True
  #horizontal
  for i in range(4): 
    if ''.join(list(set(board1[i]))) == 'X':
      return "X won"
    elif ''.join(list(set(board2[i]))) == 'O':
      return "O won"
  
  #vertical
  for i in range(4):
    if ''.join(list(set([board1[0][i], board1[1][i], board1[2][i], board1[3][i]]))) == 'X':
      return "X won"
    elif ''.join(list(set([board2[0][i], board2[1][i], board2[2][i], board2[3][i]]))) == 'O':
      return "O won"
  
  #diagonal
  if ''.join(list(set([board1[0][0], board1[1][1], board1[2][2], board1[3][3]]))) == 'X':
    return "X won"
  elif ''.join(list(set([board1[0][3], board1[1][2], board1[2][1], board1[3][0]]))) == 'X':
    return "X won"
  elif ''.join(list(set([board2[0][0], board2[1][1], board2[2][2], board2[3][3]]))) == 'O':
    return "O won"
  elif ''.join(list(set([board2[0][3], board2[1][2], board2[2][1], board2[3][0]]))) == 'O':
    return "O won"
  
  for b in board:
    if '.' in b:
      completed = False
  
  if completed: 
    return "Draw"
  else: 
    return "Game has not completed"

def main():
  f = open("A-large.in", 'rU')
  lines = f.readline()
  
  output = open('output', 'w')
  
  for i in range(int(lines)):
    board = []
    for j in range(4): 
      board.append(f.readline()[:-1])
    f.readline()
    #print board
    out = solve(board)
    output.write("Case #" + str(i+1) + ': ' + out + '\n')
    #sys.stdout.write("Case #" + str(i+1) + ": " + out + "\n")
  f.close()
  output.close()
  
if __name__ == '__main__':
  main()
