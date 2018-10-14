def complete(board):
    for row in board:
        for char in row:
            if char == '.':
                return False
    return True

def check(seq):
    if all([char == 'X' or char == 'T' for char in seq]):
        return 'X'
    if all([char == 'O' or char == 'T' for char in seq]):
        return 'O'

def game_winner(board):
    for i in range(4):
        winners = [
            check(board[i]),
            check([board[j][i] for j in range(4)]),
            ]
        for winner in winners:
            if winner is not None:
                return winner
    winners = [
        check([board[i][i] for i in range(4)]),
        check([board[3-i][i] for i in range(4)])
        ]
    for winner in winners:
        if winner is not None:
            return winner

def solve(board):
    winner = game_winner(board)
    if winner is None and complete(board):
        return "Draw"
    elif winner is None:
        return "Game has not completed"
    else:
        return winner + " won"

T = int(raw_input())
for i in range(T):
    board = [raw_input() for j in range(4)]
    print "Case #%d: %s" % (i + 1, solve(board))
    try:
        raw_input()
    except EOFError:
        # Last iteration
        pass
