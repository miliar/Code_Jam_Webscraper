import sys

def ans(R, C, M):
    def board_to_str(board):
        s = ''
        for i in range(len(board)/C):
            s += '{}\n'.format(''.join(board[i*C:i*C+C]))
        return s[:len(s)-1]

    cx = [-1, 0, 1]
    cy = [-1, 0, 1]

    def _ans(board, m):
        #print board_to_str(board)
        #print m
        #raw_input()
        if m==0 or board.count('e') == m:
            board = [ c.replace('e', '.') for c in board]
            board[0] = 'c'
            return board_to_str(board)
        for i in range(len(board)):
            if board[i] != 'e': continue
            _m = m
            backupboard = board[:]
            for _y in cy:
                for _x in cx:
                    x = _x + i % C
                    y = _y + i // C
                    if 0 <= x < C and 0 <= y < R:
                        ni = y*C + x
                        if board[ni] == '*':
                            board[ni] = 'e'
                            _m -= 1
            if board.count('e') <= m:
                board[i] = '.'
                a = _ans(board, m-1)
                if a:
                    return a
            board = backupboard
        return False

    board = ['*' for i in range(R*C)]
    board[0] = 'e'
    a = _ans(board, R*C-M)
    if a:
        return a
    else:
        return 'Impossible'
    


with open(sys.argv[1]) as fr, open(sys.argv[1] + '.out', 'w') as fw:
    T = int(fr.readline())
    for i in xrange(T):
        no = i + 1
        (R, C, M) = map(int, fr.readline().split(' '))
        fw.write("Case #{no}:\n{ans}\n".format(no=no,ans=ans(R, C, M)))

