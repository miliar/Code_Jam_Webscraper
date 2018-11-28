def solve(board):
    completed = not any(('.' in row) for row in board)
    for player in 'XO':
        row_count = [0, 0, 0, 0]
        col_count = [0, 0, 0, 0]
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell in ['T', player]:
                    row_count[i] += 1
                    col_count[j] += 1
        q1, q2 = 0, 0
        for i in range(4):
            if board[i][i] in ['T', player]:
                q1 += 1
            if board[i][3 - i] in ['T', player]:
                q2 += 1
        if 4 in row_count or 4 in col_count or q1 == 4 or q2 == 4:
            return player + ' won'
    if completed:
        return 'Draw'
    else:
        return 'Game has not completed'

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        board = [raw_input() for i in range(4)]
        raw_input()
        print 'Case #%d: %s' % (t + 1, solve(board))
