def heightValid(board):
    height = len(board)
    width = len(board[0])
    for i in range(height):
        for j in range(width):
            if not (highInRow(board, i, j) or highInCol(board, i, j)):
                return False
    return True

def highInRow(board, i, j):
    height = board[i][j]
    for w in range(len(board[0])):
        if (board[i][w] > height):
            return False
    return True

def highInCol(board, i, j):
    height = board[i][j]
    for h in range(len(board)):
        if (board[h][j] > height):
            return False
    return True

if __name__ == '__main__':
    num = int(raw_input())
    for i in range(num):
        board = []
        (n, m) = map(int, raw_input().split())
        for j in range(n):
            row = map(int, raw_input().split())
            board.append(row)
        if heightValid(board):
            print 'Case #%d: YES' % (i + 1)
        else:
            print 'Case #%d: NO' % (i + 1)
