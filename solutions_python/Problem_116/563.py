import numpy as np
import sys

# Problem

# Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

# After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

# Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:

#     "X won" (the game is over, and X won)
#     "O won" (the game is over, and O won)
#     "Draw" (the game is over, and it ended in a draw)
#     "Game has not completed" (the game is not over yet)

# If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable. 

prime_array = np.array([[2,3,5,7],[11,13,17,19],[23,29,31,37],[41,43,47,53]])

winning_numbers = [210, 20746, 42718, 46189, 48633, 123845, 141491, 260813, 765049, 4391633]

with open(sys.argv[1]) as f:
    T = int(f.readline())

    for case in xrange(T):

        g = []
        x_board = []; o_board = []
        text = ''

        for i in xrange(4):
            line = f.readline().strip()
            g.append(list(line))
            x_board.append([1 if (a=='X' or a=='T') else 0 for a in g[i]])
            o_board.append([1 if (a=='O' or a=='T') else 0 for a in g[i]])
            
        x_board = np.array(x_board * prime_array)
        o_board = np.array(o_board * prime_array)

        for i in xrange(4):
            if np.prod(x_board[i,:]) in winning_numbers:
                text = 'X won'
            if np.prod(o_board[i,:]) in winning_numbers:
                text = 'O won'

        for i in xrange(4):
            if np.prod(x_board[:,i]) in winning_numbers:
                text = 'X won'
            if np.prod(o_board[:,i]) in winning_numbers:
                text = 'O won'

        if(x_board[0,0] * x_board[1,1] * 
           x_board[2,2] * x_board[3,3] in winning_numbers):
            text = 'X won'

        if(o_board[0,0] * o_board[1,1] * 
           o_board[2,2] * o_board[3,3] in winning_numbers):
            text = 'O won'

        if(x_board[0,3] * x_board[1,2] * 
           x_board[2,1] * x_board[3,0] in winning_numbers):
            text = 'X won'


        if(o_board[0,3] * o_board[1,2] * 
           o_board[2,1] * o_board[3,0] in winning_numbers):
            text = 'O won'

        if not text:
            for i in xrange(4):
                if '.' in g[i]:
                    text = 'Game has not completed'
                    break
                else:
                    text = 'Draw'
    
            
        print "Case #%d:" % (case+1), text
#        for i in xrange(4):
#            print "%s %s %s %s" % (g[i][0],g[i][1],g[i][2],g[i][3])
        f.readline()
            
            


                
                
