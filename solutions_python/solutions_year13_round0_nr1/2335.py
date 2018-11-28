def winner(seq):
    x_count = 0
    o_count = 0
    for s in seq:
        if s == 'X':
            x_count += 1
        elif s == 'O':
            o_count += 1
        elif s == 'T':
            x_count += 1
            o_count += 1
    if x_count == 4:
        print('X won')
        return True 
    if o_count == 4:
        print('O won')
        return True
    return False

T = int(input())
for t in range(T):
    print('Case #%d:' % (t+1), end=' ')
    board = [input() for _ in range(4)]
    input()
    for i in range(4):
        if winner(board[i][j] for j in range(4)) or winner(board[j][i] for j in range(4)):
            break
    else:
        if winner(board[i][i] for i in range(4)) or winner(board[i][3-i] for i in range(4)):
            continue
        print('Game has not completed' if any('.' in r for r in board) else 'Draw')
