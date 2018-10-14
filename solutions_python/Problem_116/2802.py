import sys

def chk_rows(board):
    for y in range(4):
        solved = True
        for x in range(4):
            if board[y][x] != 'T' and board[y][x] != board[y][0]:
                solved = False
                break
        if solved and board[y][0] != '.':
            return board[y][0]

    return False

def chk_diags(board):
    solved = True
    for y in range(4):
        if board[y][y] != 'T' and board[y][y] != board[0][0]:
            solved = False
            break
    if solved and board[0][0] != '.':
        return board[0][0]

    solved = True
    for y in range(4):
        if board[y][3-y] != 'T' and board[y][3-y] != board[0][3]:
            solved = False
            break
    if solved and board[0][3] != '.':
        return board[0][3]

    return False



count = int(sys.stdin.readline())
for case in range(count):
    if case != 0:
        sys.stdin.readline()

    board = []
    for y in range(4):
        line = sys.stdin.readline()
        board.append(line[:4])

    winner = chk_rows(board)
    if winner != False:
        print('Case #{}: {} won'.format(case+1, winner.upper()))
        continue

    winner = chk_rows(list(zip(*board)))
    if winner != False:
        print('Case #{}: {} won'.format(case+1, winner.upper()))
        continue

    winner = chk_diags(board)
    if winner != False:
        print('Case #{}: {} won'.format(case+1, winner.upper()))
        continue

    full = True
    for y in range(4):
        for x in range(4):
            if board[y][x] == '.':
                full = False

    if not full:
        print('Case #{}: Game has not completed'.format(case+1))
        continue

    print('Case #{}: Draw'.format(case+1))
