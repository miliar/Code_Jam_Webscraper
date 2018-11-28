import sys
import collections

data = file(sys.argv[1]).read().strip().split("\n")

num_boards = int(data[0])

def print_result(result, board_num):
    print "Case #%d: %s" % (board_num, result)

def process(board):
    # horizontal
    for i in range(4):
        c = collections.Counter(board[i])
        for letter in ["X", "O"]:
            if c[letter] + c["T"] == 4:
                return "%s won" % (letter,)

    # verical
    for i in range(4):
        c = collections.Counter(board[j][i] for j in range(4))
        for letter in ["X", "O"]:
            if c[letter] + c["T"] == 4:
                return "%s won" % (letter,)

    # diagonal
    c = collections.Counter(board[i][i] for i in range(4))
    for letter in ["X", "O"]:
        if c[letter] + c["T"] == 4:
            return "%s won" % (letter,)

    c = collections.Counter(board[i][3 - i] for i in range(4))
    for letter in ["X", "O"]:
        if c[letter] + c["T"] == 4:
            return "%s won" % (letter,)

    # draw or complete
    if "." in [item for sublist in board for item in sublist]:
        return "Game has not completed"
    return "Draw"

board = []
board_num = 1
for line in data[1:]:
    if line:
        board.append(line)
    if len(board) == 4:
        print_result(process(board), board_num)
        board = []
        board_num += 1
