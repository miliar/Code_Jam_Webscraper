

import sys

empty = False

def test(board, state, i, j):
    global empty
    if board[i][j] == '.':
        empty = True
        return state
    elif board[i][j] == 'T':
        return (state[0], state[1], state[2] + 1)
    elif board[i][j] == 'X':
        return (state[0] + 1, state[1], state[2])
    else:
        return (state[0], state[1] + 1, state[2])

def winner(state):
    if (state[0] == 4 or state[0] == 3 and state[2] == 1) and state[1] == 0:
        return 'X'
    elif state[0] == 0 and (state[1] == 4 or state[1] == 3 and state[2] == 1):
        return 'O'
    else:
        return None

data = iter(sys.stdin)
cases = int(data.next().rstrip())
for c in xrange(cases):
    board = [data.next().rstrip(), data.next().rstrip(), data.next().rstrip(), data.next().rstrip()]
    x = False
    o = False
    empty = False

    # Rows
    for i in xrange(4):
        state = (0, 0, 0)
        for j in xrange(4):
            state = test(board, state, i, j)
        w = winner(state)
        if w == 'X':
            x = True
            break;
        elif w == 'O':
            o = True
            break;

    # Columns
    for j in xrange(4):
        state = (0, 0, 0)
        for i in xrange(4):
            state = test(board, state, i, j)
        w = winner(state)
        if w == 'X':
            x = True
            break;
        elif w == 'O':
            o = True
            break;

    # Diagonals
    state = (0, 0, 0)
    for i in xrange(4):
        state = test(board, state, i, i)
    w = winner(state)
    if w == 'X':
        x = True
    elif w == 'O':
        o = True

    state = (0, 0, 0)
    for i in xrange(4):
        state = test(board, state, i, 3 - i)
    w = winner(state)
    if w == 'X':
        x = True
    elif w == 'O':
        o = True

    if x and not o:
        print "Case #{}: {}".format(c + 1, "X won")
    elif o and not x:
        print "Case #{}: {}".format(c + 1, "O won")
    elif x and o or not empty:
        print "Case #{}: {}".format(c + 1, "Draw")
    else:
        print "Case #{}: {}".format(c + 1, "Game has not completed")
    data.next() # empty line



