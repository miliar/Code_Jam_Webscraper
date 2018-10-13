#!/usr/bin/env python

def get_board():
   board = []
   for i in range(4):
      raw_line = raw_input()
      line = []
      for i in range(len(raw_line)):
         line.append(raw_line[i])
      board.append(line)
   raw_input() # Jumps the empty line at the end
   return board

def score_analysis(score):
   if (score['X'] == 3 and score['T'] > 0) or score['X'] == 4:
      return True, 'X won'
   if (score['O'] == 3 and score['T'] > 0) or score['O'] == 4:
      return True, 'O won'
   if score['.'] > 0:
      return False, True
   return False, False

def analyse(board):
   dot = False

   # line
   for line in board:
      players = {'X' : 0, 'O' : 0, '.' : 0, 'T' : 0}

      for value in line:
         players[value] += 1

      won, result = score_analysis(players)
      if won:
         return result
      else:
         dot |=  result

   # column
   for j in range(4):
      players = {'X' : 0, 'O' : 0, '.' : 0, 'T' : 0}
      for i in range(4):
         players[board[i][j]] += 1

      won, result = score_analysis(players)
      if won:
         return result
      else:
         dot |=  result

   # diagonals
   # main
   players = {'X' : 0, 'O' : 0, '.' : 0, 'T' : 0}
   for i in range(4):
      players[board[i][i]] += 1

   won, result = score_analysis(players)
   if won:
      return result
   else:
      dot |=  result

   # secondary
   players = {'X' : 0, 'O' : 0, '.' : 0, 'T' : 0}
   for i in range(4):
      j = 3 - i
      players[board[i][j]] += 1

   won, result = score_analysis(players)
   if won:
      return result
   else:
      dot |=  result

   if dot:
      return 'Game has not completed'
   return 'Draw'

def main():
   cases = int(raw_input())
   for case in range(cases):
      board = get_board()
      print 'Case #%s: %s' %(case+1, analyse(board))

if __name__ == '__main__':
   main()
