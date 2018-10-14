#!/usr/bin/env python
""" Code Jam 2013 - Problem A """

def process(in_file):
    cases = int(in_file.readline())
    results = []
    for i in range(cases):
        # Read in board
        board = [list(in_file.readline().strip()) for x in range(4)]
        # Read blank line
        in_file.readline()

        r = check_winner(board)
        results.append("Case #%d: %s" % (i + 1, r))
    return results


def check_winner(board):
    player_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player_o = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    empty = 0

    # Check for winner
    for i in range(4):  # rows
        for j in range(4):  # cols
            if board[i][j] == 'X' or board[i][j] == 'T':
                player_x[i] += 1  # row
                player_x[4 + j] += 1  # col
                if i == j:
                    player_x[8] += 1  # diag
                elif i == (3 - j):
                    player_x[9] += 1  # anti-diag

                if 4 in player_x:
                    return "X won"

            if board[i][j] == 'O' or board[i][j] == 'T':
                player_o[i] += 1  # row
                player_o[4 + j] += 1  # col
                if i == j:
                    player_o[8] += 1  # diag
                elif i == (3 - j):
                    player_o[9] += 1  # anti-diag

                if 4 in player_o:
                    return "O won"

            if board[i][j] == '.':
                empty += 1

    if not empty:
        return "Draw"
    else:
        return "Game has not completed"


if __name__ == '__main__':
    import sys

    # Read args
    if len(sys.argv) < 2:
        print "USAGE: gjA in_file.in out_file.out"

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file, 'rU') as f:
        result = process(f)

    with open(out_file, 'w') as f:
        for line in result:
            f.write("%s\n" % line)
