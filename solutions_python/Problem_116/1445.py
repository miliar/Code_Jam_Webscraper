import sys

def check(subboard):
    for player in ("O", "X"):
        cur_subboard = subboard.replace("T", player)
        if cur_subboard == player*4:
            return True
    return False

def identify_winner(subboard):
    if subboard[0] != 'T':
        return subboard[0]
    return subboard[1]

def solve(board):
    # Win on row
    for row in xrange(4):
        start = row*4
        subboard = board[start:start+4]
        if check(subboard):
            return identify_winner(subboard)


    # Win on column
    for col in xrange(4):
        start = col
        subboard = board[col::4]
        if check(subboard):
            return identify_winner(subboard)

    # Win on diagonal
    subboard = board[0::5]
    if check(subboard):
        return identify_winner(subboard)
    subboard = board[3:-1:3]
    if check(subboard):
        return identify_winner(subboard)

    if '.' in board:
        return "."
    else:
        return "D"

def single_case():
    board = ''.join([raw_input() for i in xrange(4)])
    return solve(board)

messages = {
    'X': "X won",
    'O': "O won",
    'D': "Draw",
    '.': "Game has not completed",
}

t = int(raw_input())
for i in xrange(t):
    outcome = single_case()
    print "Case #{0}: {1}".format(i+1, messages[outcome])
    try:
        raw_input()
    except EOFError:
        sys.exit(0)

