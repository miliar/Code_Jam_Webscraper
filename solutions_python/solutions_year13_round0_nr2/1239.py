import sys
import numpy as np


def solve_board(board):
    board = np.array(board)
    max_rows = np.amax(board,axis=1)
    max_cols = np.amax(board,axis=0)

    for n in range(len(board)):
        for m in range(len(board[0])):
            val = board[n][m]
            if max_rows[n] != val and max_cols[m] != val:
                return "NO"

    return "YES"


def solve_problem(istream, ostream):

    num_testcases = int(istream.readline().strip())

    for t in range(1, num_testcases+1):
        n,m = istream.readline().split()
        n = int(n)
        m = int(m)
        board = []
        for i in range(n):
            board.append([int(x) for x in istream.readline().split()])

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
