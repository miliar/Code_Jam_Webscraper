indice = range(4)
def won(board, x):
    for i in indice:
        if all(board[i][j] in (x, 'T') for j in indice):
            return True
    for i in indice:
        if all(board[j][i] in (x, 'T') for j in indice):
            return True
    return (
        all(board[i][i] in (x, 'T') for i in indice) or
        all(board[i][-i-1] in (x, 'T') for i in indice)
    )

def solve(board):
    if won(board, 'X'): return 'X won'
    if won(board, 'O'): return 'O won'
    return 'Game has not completed' if '.' in ''.join(board) else 'Draw'

for case in range(1, input()+1):
    board = [raw_input() for _ in range(4)]
    raw_input()
    print 'Case #{}: {}'.format(case, solve(board))
