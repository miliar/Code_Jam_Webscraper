import sys
import numpy as np

def test_items(a):
    a.discard('T')
    if len(a) > 1:
        return False, "Nopes"

    val = a.pop()
    if val == 'O':
        return True, "O won"
    if val == 'X':
        return True, "X won"


    return False, "Nopes"

def solve_board(board):
    for row in range(4):
        t,r = test_items({board[row][i] for i in range(4)})
        if t:
            return r

    for col in range(4):
        t,r = test_items({board[i][col] for i in range(4)})
        if t:
            return r

    t,r = test_items({board[i][i] for i in range(4)})
    if t:
        return r

    t,r = test_items({board[i][3-i] for i in range(4)})
    if t:
        return r

    for row in range(4):
        if '.' in board[row]:
            return "Game has not completed"

    return "Draw"


def solve_problem(istream, ostream):

    num_testcases = int(istream.readline().strip())

    for t in range(1, num_testcases+1):

        board = []
        for i in range(4):
            board.append(istream.readline())

        istream.readline()

        print("Case #{:d}: {:s}".format(t, solve_board(board)), file=ostream)




if __name__ == "__main__":
    if len(sys.argv) > 1:
        istream = open(sys.argv[1])
    else:
        istream = sys.stdin

    if len(sys.argv) > 2:
        ostream = open(sys.argv[2])
    else:
        ostream = sys.stdout

        solve_problem(istream,ostream)
