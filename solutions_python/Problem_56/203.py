def check_k(board, rb, K):
    for row in board:
        if rb != 1:
            if 'R'*K in row:
                rb += 1
        if rb != 2:
            if 'B'*K in row:
                rb += 2
        if rb == 3:
            break
    return rb

T = int(raw_input())
for i in range(T):
    [N, K] = map(int, raw_input().split(' '))
    board = []
    for j in range(N):
        board.append(''.join(reversed(raw_input().replace('.',''))))
    rb = 0
    rb = check_k(board, rb, K)
    if rb < 3:
        rot_board = []
        for l in range(N):
            col = ''
            for row in board:
                try:
                    col += row[l]
                except:
                    pass
            rot_board.append(col)
        rb = check_k(rot_board, rb, K)
    if rb < 3:
        diag1_board = []
        for l in range(2*N-1):
            diag = ''
            for m in range(l+1):
                try:
                    diag += board[m][l-m]
                except:
                    pass
            diag1_board.append(diag)
        rb = check_k(diag1_board, rb, K)
    if rb < 3:
        diag2_board = []
        for l in range(2*N-1):
            diag = ''
            for m in range(l+1):
                try:
                    diag += board[N-m][l-m]
                except:
                    pass
            diag2_board.append(diag)
        rb = check_k(diag2_board, rb, K)

    results = ['Neither', 'Red', 'Blue', 'Both']
    print 'Case #%d: %s' % (i+1, results[rb])




        
    