from collections import Counter


def check_vertical(board, i, player):

    
    for j in [0, 1, 2, 3]:
        if board[i][j] == player: continue
        if board[i][j] == 'T': continue
        return None

    return player + ' won'

def check_horizontal(board, i, player):

    for j in [0, 1, 2, 3]:
        if board[j][i] == player: continue
        if board[j][i] == 'T': continue
        return None

    return player + ' won'

def check_left_diagonal(board, player):
    
    for i in [0, 1, 2, 3]:
        if board[i][i] == player: continue
        if board[i][i] == 'T': continue
        return None

    return player + ' won'

def check_right_diagonal(board, player):
    
    for i in [0, 1, 2, 3]:
        if board[i][3-i] == player: continue
        if board[i][3-i] == 'T': continue
        return None

    return player + ' won'

def check_draw(board):

    for i in [0, 1, 2, 3]:
        for j in [0, 1, 2, 3]:
            if board[i][j] == '.': return None

    return 'Draw'

    

def solve(board):

    for player in ['O', 'X']:
        for i in [0, 1, 2, 3]:
            ret = check_horizontal(board, i, player)
            if ret: return ret

            ret = check_vertical(board, i, player)
            if ret: return ret

        ret = check_left_diagonal(board, player)
        if ret: return ret

        ret = check_right_diagonal(board, player)
        if ret: return ret

    ret = check_draw(board)

    if ret: return ret

    return 'Game has not completed'



    return 1

if __name__ == '__main__':

    import sys
    
    input_file = sys.argv[1]
    output_file = input_file[:].replace('.in', '.out')


    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')

    T, = [int(x) for x in f_in.readline().split()]

    for case in range(1, T+1):
        print 
        print '====================='
        print '    ' + str(case)
        print '====================='

        board = []

        board.append(f_in.readline().strip())
        board.append(f_in.readline().strip())
        board.append(f_in.readline().strip())
        board.append(f_in.readline().strip())

        # empty line
        f_in.readline()

        # Solve
        ans = solve(board)

        print ans

        ## Output
        f_out.write('Case #%d: %s\n' % (case, ans))

        

