#!/usr/bin/python
import sys,os
from operator import itemgetter

def solve(board):
    """Returns a string result to one case of a problem
    All possible outputs:
        "X won"
        "O won"
        "Draw"
        "Game has not completed"
    """
    winner = do_we_have_winner(board)
    if winner:
        return "%s won" % winner
    else:
        return "Draw" if is_completed(board) else "Game has not completed"
    return "OMGnowai!"

def do_we_have_winner(board):
    # check all rows
    # check all columns
    for i in range(4):
        row_winner = winning_segment(get_row(board, i))
        col_winner = winning_segment(get_col(board, i))
        if row_winner:return row_winner
        if col_winner:return col_winner
    # check \ (down) diagonal
    down_diag_winner = winning_segment(get_down_diagonal(board))
    if down_diag_winner: return down_diag_winner
    # check / (up) diagonal
    up_diag_winner = winning_segment(get_up_diagonal(board))
    if up_diag_winner: return up_diag_winner

def is_completed(board):
    for e_row in board:
        for e_cell in e_row:
            if e_cell == ".": return False
    return True

def get_row(matrix, row):
    return matrix[row]

def get_col(matrix, col):
    return [itemgetter(col)(i) for i in matrix]

def get_down_diagonal(matrix):
    segment = []
    i = 0
    for e_row in matrix:
        segment.append(e_row[i])
        i += 1
    return segment

def get_up_diagonal(matrix):
    segment = []
    i = len(matrix) - 1
    for e_row in matrix:
        segment.append(e_row[i])
        i -= 1
    return segment

def winning_segment(segment):
    """ Returns winner {'X','O'} or False 
    """
    seg_set = set(segment)
    len_seg_set = len(seg_set)
    if len_seg_set == 1: # only one type of char in segment, either winner or empty
        if set(["."]) == seg_set:
            return False # Is empty line
        return seg_set.pop() # Return winner
    if len_seg_set == 2 and "T" in seg_set:
        if "O" in seg_set:
            return "O"
        if "X" in seg_set:
            return "X"
    return False

#Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        cases = int(f_in.readline().strip())
        for case in range(1,cases+1):
            #Get input data
            board = []
            for row in range(4):
                board.append(list(x for x in f_in.readline().strip()))
            f_in.readline() # One empty line after each board
            #Solve and output
            print("Case #{}: {}".format(case, solve(board)))
    
if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '"+str(sys.argv[1])+"' does not exist!"
    else:
        print "No file supplied! Run program this way: '"+str(sys.argv[0])+" something.in'"

