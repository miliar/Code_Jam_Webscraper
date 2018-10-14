#!/usr/bin/python

solution = open('small.out', 'w')

def answer(case, output):
    solution.write('Case #%d: %s\n' % (case, output))

def check_won(case, game):
    for player in ['X', 'O']:
        if game.replace('T', player) == player * 4:
            answer(case, '%s won' % player)
            return True
    return False

def solve(case, board, dot_found):
    leftdiag = ''
    rightdiag = ''
    won = False
    for col in xrange(4):
        colstr = ''.join([row[col] for row in board])
        if not won:
            won = check_won(case, colstr)

        leftdiag += board[col][col]
        rightdiag += board[col][3 - col]

    if not won:
        won = check_won(case, leftdiag)
    if not won:
        won = check_won(case, rightdiag)
    if not won:
        if dot_found:
            answer(case, 'Game has not completed')
            won = True
        else:
            answer(case, 'Draw')
            won = True

T = raw_input()
for case in xrange(1, int(T) + 1):
    board = []
    won = False
    dot_found = False
    for i in xrange(4):
        row = raw_input()
        if '.' in row:
            dot_found = True
        if check_won(case, row):
            won = True
        board.append(list(row))
    if case < T:
        raw_input()

    if not won:
        solve(case, board, dot_found)

