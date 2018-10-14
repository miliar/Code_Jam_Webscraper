""" 
Code Jam 2013
Problem: Tic-Tac-Toe-Tomek
Usages: 
  $ python script < input > output
  PS > gc input | python script | sc output.
"""

import sys

def check(board, size=4):
    slines = [''.join(sorted(line)) for line in lines(board, size)]
    if any(l in slines for l in ['X'*size, "TXXX"]):
        return "X won"
    elif any(l in slines for l in ['O'*size, "OOOT"]):
        return "O won"
    elif any(l[0]=='.' for l in slines):
        return "Game has not completed"
    else:
        return "Draw"

def lines(board, size=4):
    h = [board[i:i+size] for i in range(0, len(board), size)]
    v = [''.join([board[i] for i in range(i, len(board), size)]) for i in range(size)]
    d = ([''.join([board[size*i+i] for i in range(size)])] +
         [''.join([board[size*i-i] for i in range(1, size+1)])])
    return h + v + d

if __name__ == '__main__':
    size = 4
    numcases = int(sys.stdin.readline().strip())
    for i in range(1, numcases+1):
        board = ''.join([sys.stdin.readline().strip() for row in range(size)])
        sys.stdin.readline()
        result = check(board)
        print "Case #%d: %s" % (i, result)
