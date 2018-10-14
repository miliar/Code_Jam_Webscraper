# -*- coding: utf-8 -*-
#Filename: calc_prob.py

import sys
import copy

class TicTacToeTomek:

    def __init__(self, input_filename, output_filename):
        
        # Open input and output files
        input_file = open(input_filename, 'r')
        output_file = open(output_filename, 'w')
        
        # Get the number of boards
        number_of_boards = int(input_file.readline())
        
        # Evaluate all board positions and output the result to the output file
        for case in range(number_of_boards):
            board_repr = self.read_board(input_file)
            result = self.eval_board(board_repr)
            self.output_result(result, case+1, output_file)
        
    def read_board(self, input_file):
        board_repr = []
        for i in range(4):
            board_repr.append(input_file.readline()[:-1])
        
        # Read empty line in order to remove it
        input_file.readline()
        
        return board_repr
        
    
    def eval_board(self, board):
        
        # First create all rows, columns, and diagonals
        
        # Rows
        groups = copy.deepcopy(board)
        
        # Columns
        for i in range(4):
            col = board[0][i]+board[1][i]+board[2][i]+board[3][i]
            groups.append(col)
        
        # Diagonals
        groups.append(board[0][0]+board[1][1]+board[2][2]+board[3][3])
        groups.append(board[0][3]+board[1][2]+board[2][1]+board[3][0])
        
        # Determine winning groups
        x_wins = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
        o_wins = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']
        
        for group in x_wins:
            if group in groups:
                return 1
        for group in o_wins:
            if group in groups:
                return -1
        
        # If the game is not won, check if it has completed
        for group in board:
            if '.' in group:
                return -2
        
        # Else, it must be a draw
        return 0
        
    
    def output_result(self, result, case_nr, output_file):
        if result == 1:
            output_file.write('Case #{}: X won\n'.format(case_nr))
        elif result == 0:
            output_file.write('Case #{}: Draw\n'.format(case_nr))
        elif result == -1:
            output_file.write('Case #{}: O won\n'.format(case_nr))
        else:
            output_file.write('Case #{}: Game has not completed\n'.format(case_nr))

def main(args):
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    
    if len(args) == 1:
        input_filename = args[0]
    elif len(args) == 2:
        input_filename = args[0]
        output_filename = args[1]
    else:
        print 'Too many input arguments. Executing with default input and output filename'
    
    TicTacToeTomek(input_filename, output_filename)


if __name__ == '__main__':
    main(sys.argv[1:])
