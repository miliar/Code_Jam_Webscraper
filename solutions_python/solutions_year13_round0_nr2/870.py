
def solve(board, board_rotated, n, m):
    el = board[n][m]
    line = board[n]
    col = board_rotated[m]
    if el < max(line) and el < max(col):
        return 'NO'
    return ''

def solve_board(board, N, M):
    board_rotated = []
    for m in range(0, M):
        board_rotated.append([board[i][m] for i in range(0, N)])

    for n in range(0, N):
        for m in range(0, M):
            res = solve(board, board_rotated, n, m)
            if res != '':
                return res
    return 'YES'

def main():
    T = int(raw_input())
    for t in range(0, T):
        N, M = map(int, raw_input().split(' '))
        board = [map(int, raw_input().split(' ')) for b in range(0, N)]
        res = solve_board(board, N, M)

        print 'Case #{}: {}'.format(t+1, res)

main()
