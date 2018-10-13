n_cases = int(raw_input())

for case in xrange(1, n_cases + 1):

    N, K = map(int, raw_input().split())

#    print N, K
    board = []
    for y in xrange(N):
        board.append(raw_input())

    def print_board(board):
        for row in board:
            print ''.join(row)

    board = reversed(board)
    rotated = []

    for row in board:
        row = ''.join([c for c in row if c != '.'])
        row = row.rjust(N, '.')
        rotated.append(list(row))

    DIRECTIONS = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    def find_four(board):
        for (dx, dy) in DIRECTIONS:
            mx = min(N, N - (K - 1) * dx)
            my = min(N, N - (K - 1) * dy)
            for sx in xrange(mx):
                for sy in xrange(my):
                    assert 0 <= sx < N
                    assert 0 <= sy < N

    #                print sx, sy
                    four = board[sy][sx]
    #                print four
                    if four == '.':
                        continue

                    for d in xrange(1, K):
                        x = sx + dx * d
                        y = sy + dy * d

                        if not (0 <= x < N and 0 <= y < N):
                            break

                        if board[y][x] != four:
                            break
                    else:
                        yield four

    # apply gravity
    #print
    #print_board(rotated)
    found = list(find_four(rotated))
    if 'R' in found:
        if 'B' in found:
            result = 'Both'
        else:
            result = 'Red'
    elif 'B' in found:
        result = 'Blue'
    else:
        result = 'Neither'

    print 'Case #%d: %s' % (case, result)

    #print
    #print_board(rotated)

