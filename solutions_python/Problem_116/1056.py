"Google jam: https://code.google.com/codejam/contest/2270488/dashboard"

P1 = 'X'
P2 = 'O'
EMPTY = '.'
JOCKER = 'T'
SIZE = 4


def _check_winner(line, player):
    "Return True if player won in the line else False."
    c = line.count(player)
    return c == 4 or (c == 3 and JOCKER in line)


def solve(board):
    # Check rows.
    for row in board:
        if _check_winner(row, P1):
            return 'X won'
        if _check_winner(row, P2):
            return 'O won'
    # Check columns.
    for col in zip(*board):
        if _check_winner(col, P1):
            return 'X won'
        if _check_winner(col, P2):
            return 'O won'
    # Check diagonals.
    diagonals = [
        [board[i][i] for i in range(SIZE)],
        [board[i][SIZE - 1 - i] for i in range(SIZE)]
    ]
    for diagonal in diagonals:
        if _check_winner(diagonal, P1):
            return 'X won'
        if _check_winner(diagonal, P2):
            return 'O won'
    # If no one won check that the game is completed or no.
    for row in board:
        if EMPTY in row:
            return 'Game has not completed'
    return 'Draw'


def main():
    t = int(raw_input())
    for i in range(t):
        board = [raw_input() for _ in range(SIZE)]
        res = solve(board)
        print "Case #%d: %s" % (i + 1, res)
        if i < t - 1:
            raw_input() # Drop empty line between test cases.


if __name__ == "__main__":
    main()
