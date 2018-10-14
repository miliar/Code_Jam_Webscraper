

def read_board():
    board = [raw_input() for i in range(0, 4)]
    return board

def solve(board, x, y, right=0, down=0):
    count_X, count_O = 0, 0
    res = ''
    for i in range(0, 4):
        el = board[y][x]
        if el == 'X':
            count_X += 1
        elif el == 'O':
            count_O += 1
        elif el == 'T':
            count_X += 1
            count_O += 1
        x += right
        y += down
    if count_X == 4:
        res = 'X won'
    elif count_O == 4:
        res = 'O won'
    return res

def solve_board(board):
    # check column
    for x in range(0, 4):
        res = solve(board, x, 0, down=1)
        if res != '':
            return res
    # check line
    for y in range(0, 4):
        res = solve(board, 0, y, right=1)
        if res != '':
            return res
    # check diagonals
    res = solve(board, 0, 0, right=1, down=1)
    if res != '':
        return res
    res = solve(board, 0, 3, right=1, down=-1)
    if res != '':
        return res
    # check over
    if '.' in ''.join(board):
        return 'Game has not completed'
    return 'Draw'

def main():
    T = int(raw_input())
    for i in range(0, T):
        if i > 0:
            raw_input() #flush the \n separator
        board = read_board()
        res = solve_board(board)
        print 'Case #{}: {}'.format(i+1, res)

main()
