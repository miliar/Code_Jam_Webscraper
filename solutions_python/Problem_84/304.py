from __future__ import division
import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )

def solve(board, r, c):
    board = board[:]
    possible = True
    for i in xrange(r-1):
        if possible == False:
            break
        for j in xrange(c-1):
            if board[i][j] == '#':
                if board[i][j+1] == '#' and board[i+1][j] == '#' and board[i+1][j+1] == '#':
                    board[i] = board[i][:j] + "/\\" + board[i][j+2:]
                    board[i+1]= board[i+1][:j] + "\\/" + board[i+1][j+2:]
                else:
                     possible = False
                     break
    
    if possible:
        for i in xrange(r):
            if possible == False:
                break
            for j in xrange(c):
                if board[i][j] == '#':
                    possible = False
                    break
    return (possible, board)
    
def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            
            (r, c) = [int(x) for x in input_f.readline().split(" ")]
            board = []
            for i in xrange(r):
                row = input_f.readline().strip()
                board.append(row)
            
            (possible, upd_board) = solve(board, r, c)
            
            output_f.write("Case #%d:\n" % (test_case_i + 1))
            if not possible:
                output_f.write("Impossible\n")
            else:
                for i in xrange(len(upd_board)):
                    output_f.write("%s\n" % upd_board[i])
    
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
