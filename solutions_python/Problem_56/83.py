def rotate(board):
    n = len(board)
    result = [[' '] * n for _ in range(n)]
    for r in xrange(n):
        for c in xrange(n):
            result[c][n-1-r] = board[r][c]
    return result

def rg(board):
    #board = board.split()
    n = len(board)
    board = [line.replace('.', '').rjust(n, '.') for line in board]
    return rotate(board)

def win(board, who, K):
    n = len(board)
    # up -> down
    for j in range(n):
        c = 0
        for i in range(n):
            if board[i][j] != who:
                c = 0
                continue
            c += 1
            if c == K:
                return True
    # left -> right
    for i in range(n):
        c = 0
        for j in range(n):
            if board[i][j] != who:
                c = 0
                continue
            c += 1
            if c == K:
                return True
    # -> right/down
    for i, j in [(i,0) for i in range(n)] + [(0,i) for i in range(1,n)]:
        c = 0
        while i < n and j < n:
            if board[i][j] != who:
                c = 0
            else:
                c += 1
                if c == K:
                    return True
            i += 1
            j += 1
    # -> left/down
    for i, j in [(i,n-1) for i in range(n)] + [(0,i) for i in range(n-1)]:
        c = 0
        while i < n and j >= 0:
            if board[i][j] != who:
                c = 0
            else:
                c += 1
                if c == K:
                    return True
            i += 1
            j -= 1
    return False

def solve(K, board):
    board = rg(board)
    #print '--'
    #print '\n'.join(map(''.join, board))
    R = win(board, 'R', K)
    B = win(board, 'B', K)
    return ['Neither', 'Blue', 'Red', 'Both'][R << 1 | B]

if __name__ == '__main__':
    import sys
    rl = iter(sys.stdin).next
    for i in range(1, int(rl())+1):
        N, K = map(int, rl().split())
        board = [rl().strip() for _ in range(N)]
        print 'Case #%d: %s' % (i, solve(K, board))
