def process(board):
    for i in xrange(4):
        if all(board[i][j] in ('X', 'T') for j in xrange(4)):
            return 'X won'
        elif all(board[i][j] in ('O', 'T') for j in xrange(4)):
            return 'O won'
        elif all(board[j][i] in ('X', 'T') for j in xrange(4)):
            return 'X won'
        elif all(board[j][i] in ('O', 'T') for j in xrange(4)):
            return 'O won'
    if all(board[i][i] in ('X', 'T') for i in xrange(4)):
        return 'X won'
    elif all(board[i][i] in ('O', 'T') for i in xrange(4)):
        return 'O won'
    elif all(board[i][3-i] in ('X', 'T') for i in xrange(4)):
        return 'X won'
    elif all(board[i][3-i] in ('O', 'T') for i in xrange(4)):
        return 'O won'
    elif any('.' in line for line in board):
        return 'Game has not completed'
    else:
        return 'Draw'

masks = [
    0xF, 0xF0, 0xF00, 0xF000,
    0x1111, 0x2222, 0x4444, 0x8888,
    0x1248, 0x8421,
]


def process2(board):
    x = 0
    o = 0
    for i, c in enumerate(''.join(board)):
        if c == 'X':
            x |= 1 << i
        elif c == 'O':
            o |= 1 << i
        elif c == 'T':
            x |= 1 << i
            o |= 1 << i
    for m in masks:
        if x & m == m:
            return 'X won'
        elif o & m == m:
            return 'O won'
    if x | o == 0xFFFF:
        return 'Draw'
    else:
        return 'Game has not completed'

N = int(raw_input())
for n in xrange(1, N + 1):
    board = [raw_input() for _ in xrange(4)]
    try:
        raw_input()
    except EOFError:
        pass
    result = process2(board)
    print 'Case #{0}:'.format(n), result
