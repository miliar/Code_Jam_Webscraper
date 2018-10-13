#lines = open('A-test.in', 'r').read().strip().split('\n')
lines = open('A-large.in', 'r').read().strip().split('\n')
# lines = open('A-large.in', 'r').read().strip().split('\n')
T = int(lines[0])

board = []

def solveit(board, R, C):
    i = 0
    while i < R:
        j = 0
        while j < C:
            if board[i][j] != '?':
                k = j + 1
                while k < C:
                    if board[i][k] == '?':
                        board[i] = board[i][:k] + board[i][j] + board[i][k+1:]
                    else:
                        break
                    k += 1

                k = j - 1
                while k >= 0:
                    if board[i][k] == '?':
                        board[i] = board[i][:k] + board[i][j] + board[i][k+1:]
                    else:
                        break
                    k -= 1

            j += 1
        i += 1

    i = 1
    while i < R:
        if board[i] == '?' * C:
            board[i] = board[i-1]
        i += 1
    
    i = R-2
    while i >= 0:
        if board[i] == '?' * C:
            board[i] = board[i+1]
        i -= 1

    return board

ln = 1
i = 0
while i < T:
    R = int(lines[ln].split()[0])
    C = int(lines[ln].split()[1])
    board = []

    j = 0
    while j < R:
        board.append(lines[ln + j + 1])
        j += 1

    ln += R + 1
    i += 1
    board = solveit(board, R, C)
    print 'Case #' + str(i) + ':'
    for k in range(R):
        print board[k]
