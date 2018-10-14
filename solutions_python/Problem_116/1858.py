# Qualification Round 2013
# https://code.google.com/codejam/contest/2270488/dashboard#s=p0

#Problem

# Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

#After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

#Given an 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:

#    "X won" (the game is over, and X won)
#    "O won" (the game is over, and O won)
#    "Draw" (the game is over, and it ended in a draw)
#    "Game has not completed" (the game is not over yet)


#Input

#The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line. 

#Output

#For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on. 

#Limits

#The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
#Small dataset

#1 = T = 10.
#Large dataset

#1 = T = 1000. 

import sys

def solve(g):
    x = 'X won'
    o = 'O won'
    d = 'Draw'
    
    x_wins = ('TXXX', 'XXXX')
    o_wins = ('OOOT', 'OOOO')
    
    rows = []
    cols = []
    
    incomplete = False
    for i in range(0, 4):
      rows.append("".join(sorted(g[i])))
      cols.append("".join(sorted([g[0][i],g[1][i],g[2][i],g[3][i]])))
      if rows[-1] in x_wins or cols[-1] in x_wins:
         return x
      if rows[-1] in o_wins or cols[-1] in o_wins:
         return o
      if '.' in rows[-1] or '.' in cols[-1]:
         incomplete = True

    diag1 = "".join(sorted([g[0][0],g[1][1],g[2][2],g[3][3]]))
    if diag1 in x_wins:
      return x
    if diag1 in o_wins:
      return o
    diag2 = "".join(sorted([g[0][3],g[1][2],g[2][1],g[3][0]]))
    if diag2 in x_wins:
      return x
    if diag2 in o_wins:
      return o

    if incomplete == True:
      return 'Game has not completed'
      
    return d

def save_line(game, i):
    game[i] = list(f.readline().strip())
    
def process_problem(n):
    game = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
    save_line(game, 0)
    save_line(game, 1)
    save_line(game, 2)
    save_line(game, 3)
    f.readline()
    #print game
    answer = solve(game)
    print "Case #%d: %s" % (n, answer)

f = open(sys.argv[1], 'r')
T = int(f.readline())
for n in range(0, T):
    process_problem(n+1)
