# Tic-Tac-Toe-Tomek

##FILE_NAME = 'A-sample'
##FILE_NAME = 'A-small-attempt0'
FILE_NAME = 'A-large'
##FILE_NAME = 'A-small-practice'

from itertools import chain

def check_path(path, chk_pc):
    for pc in path:
        if pc != chk_pc and pc != 'T':
            return False
    else:
        return True

def do_case():
    board = tuple(tuple(pc for pc in get_line()) for r in range(4))
    get_line() # ignore extra line
    
    for chk_pc in ('X', 'O'):
        # check rows
        for row in board:
            if check_path(row, chk_pc):
                return '{} won'.format(chk_pc)
        # check columns
        for c in range(4):
            if check_path((board[r][c] for r in range(4)), chk_pc):
                return '{} won'.format(chk_pc)
        # check forward diagonol
        if check_path((board[r][r] for r in range(4)), chk_pc):
            return '{} won'.format(chk_pc)
        # check backward diagonol
        if check_path((board[r][-r-1] for r in range(4)), chk_pc):
            return '{} won'.format(chk_pc)
    
    # check for blank spaces
    if '.' in chain.from_iterable(board):
        return 'Game has not completed'
    else:
        return 'Draw'
    
with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}.out'.format(FILE_NAME), 'w') as fout:
        get_line = lambda: fin.readline()[:-1]
        get_split = lambda: get_line().split()
        get_ints = lambda: (int(i) for i in get_split())
        get_iter = lambda: (item for item in get_split())
        case_out = lambda result: fout.write('Case #{}: {}\n'.format(case, result))
        num_cases = next(get_ints())
        for case in range(1, num_cases+1):
            result = do_case()
            case_out(result)

print('done.')
