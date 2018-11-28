import sys

def read_input():
    lines = input()

    boards = []
    for i in range(lines):
        board = []

        i = "1"
        while i.strip():
            i = sys.stdin.readline().strip()
            if i: board.append(i)

        boards.append(board)

    return boards

def won(l):
    for i in ['O', 'X']:
        for j in l:
            if j != i and j != 'T':
                break
        else:
            return i

def generate_cases(board):
    for i in board:
        yield i

    for m in range(4):
        yield ''.join([board[t][m] for t in range(4)])

    yield ''.join([board[m][m] for m in range(4)])
    yield ''.join([board[m][4 - m - 1] for m in range(4)])

def solve_board(board, num):
    for case in generate_cases(board):
        j = won(case)
        if j:
            print "Case #%d: %s won" % (num, j)
            return

    if ''.join(board).find('.') < 0:
        print "Case #%d: Draw" % (num)
        return

    print "Case #%d: Game has not completed" % (num)


def solve():
    boards = read_input()
    for i, board in enumerate(boards):
        solve_board(board, i+1)


solve()
