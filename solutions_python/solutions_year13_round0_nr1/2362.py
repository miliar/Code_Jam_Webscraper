import sys


RESULTS = [
    "Draw",
    "Game has not completed",
    "O won",
    "X won",
]


def check_win(row):
    cnt, player = 0, None
    for elt in row:
        if player == '.':
            pass
        elif elt == 'T':
            cnt += 1
        elif player is None:
            player = elt
            cnt += 1
        elif player == elt:
            cnt += 1
    if cnt == 4:
        return player
    return None


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        for nb_testcase in range(int(file.readline())):
            result = RESULTS[0]
            board = {}
            for i in range(4):
                for j, val in enumerate(file.readline()):
                    if val == '.':
                        result = RESULTS[1]
                    board[(i, j)] = val
            file.readline()  # discard empty line
            rows = [
                #lines
                (board[0, j] for j in xrange(4)),
                (board[1, j] for j in xrange(4)),
                (board[2, j] for j in xrange(4)),
                (board[3, j] for j in xrange(4)),
                # columns
                (board[i, 0] for i in xrange(4)),
                (board[i, 1] for i in xrange(4)),
                (board[i, 2] for i in xrange(4)),
                (board[i, 3] for i in xrange(4)),
                # diagonals
                (board[i, i] for i in xrange(4)),
                (board[3 - i, i] for i in xrange(4)),
            ]
            for row in rows:
                player = check_win(row)
                if player is not None:
                    result = RESULTS[2 if player == 'O' else 3]
                    break
            print "Case #%d: %s" % (nb_testcase+1, result)
