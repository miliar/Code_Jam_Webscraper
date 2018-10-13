import sys

toks = open(sys.argv[1], 'r').read().split()
toks.reverse()

T = int(toks.pop())
for t in xrange(T):
    N = int(toks.pop())
    M = int(toks.pop())

    board = {}

    free_rows = set(xrange(1, N+1))
    free_cols = set(xrange(1, N+1))
    free_dia1 = set(xrange(2, 2*N+1))
    free_dia2 = set(xrange(-N+1, N))

    total_val = 0

    for m in xrange(M):
        type = toks.pop()
        row = int(toks.pop())
        col = int(toks.pop())

        board.setdefault((row, col), 0)
        if type in 'xo':
            board[row, col] |= 1
            free_rows.remove(row)
            free_cols.remove(col)
            total_val += 1

        if type in '+o':
            board[row, col] |= 2
            free_dia1.remove(row+col)
            free_dia2.remove(col-row)
            total_val += 1

    new_board = dict(board)

    for row in free_rows:
        rook = row, free_cols.pop()
        new_board.setdefault(rook, 0)
        new_board[rook] |= 1
        total_val += 1

    for dia2 in sorted(free_dia2, key=lambda d: -abs(d)):
        for dia1 in free_dia1:
            if dia1 % 2 != abs(dia2) % 2:
                continue
            col = (dia1 + dia2) // 2
            row = (dia1 - dia2) // 2
            if not (1 <= col <= N) or not (1 <= row <= N):
                continue

            bishop = (row, col)
            new_board.setdefault(bishop, 0)
            new_board[bishop] |= 2
            total_val += 1
            free_dia1.remove(dia1)
            break

    new_pieces = []
    for piece, val in new_board.iteritems():
        if board.get(piece, 0) != val:
            new_pieces.append(('x+o'[val-1], piece[0], piece[1]))

    print 'Case #{}: {} {}'.format(t+1, total_val, len(new_pieces))
    for type, row, col in new_pieces:
        print '{} {} {}'.format(type, row, col)
