import sys

def winner(board):
    # rows
    for row in board:
        chars = {}
        for char in row:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1
        if 'O' in chars and (chars['O'] == 4 or (chars['O'] == 3 and 'T' in chars and chars['T'] == 1)):
             return 'O won'
        elif 'X' in chars and (chars['X'] == 4 or (chars['X'] == 3 and 'T' in chars and chars['T'] == 1)):
             return 'X won'
    # columns
    for i in range(0, 4):
        chars = {}
        for j in range(0, 4):
            if board[j][i] not in chars:
                chars[board[j][i]] = 0
            chars[board[j][i]] += 1
        if 'O' in chars and (chars['O'] == 4 or (chars['O'] == 3 and 'T' in chars and chars['T'] == 1)):
             return 'O won'
        elif 'X' in chars and (chars['X'] == 4 or (chars['X'] == 3 and 'T' in chars and chars['T'] == 1)):
             return 'X won'

    # diag
    chars = {}
    for i in range(0, 4):
        if board[i][i] not in chars:
            chars[board[i][i]] = 0
        chars[board[i][i]] += 1
    if 'O' in chars and (chars['O'] == 4 or (chars['O'] == 3 and 'T' in chars and chars['T'] == 1)):
         return 'O won'
    elif 'X' in chars and (chars['X'] == 4 or (chars['X'] == 3 and 'T' in chars and chars['T'] == 1)):
         return 'X won'

    chars = {}
    for i in range(0, 4):
        if board[i][3-i] not in chars:
            chars[board[i][3-i]] = 0
        chars[board[i][3-i]] += 1
    if 'O' in chars and (chars['O'] == 4 or (chars['O'] == 3 and 'T' in chars and chars['T'] == 1)):
         return 'O won'
    elif 'X' in chars and (chars['X'] == 4 or (chars['X'] == 3 and 'T' in chars and chars['T'] == 1)):
         return 'X won'

    # draw
    chars = {}
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] not in chars:
                chars[board[i][j]] = 0
            chars[board[i][j]] += 1
    if '.' not in chars:
        return 'Draw'

    return 'Game has not completed'

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    for ff in xrange(0, int(f.readline())):
        board = []
        for i in range(0, 4):
            board.append(list(f.readline()))
        print 'Case #%d: %s' % (ff + 1, winner(board))
        f.readline()
