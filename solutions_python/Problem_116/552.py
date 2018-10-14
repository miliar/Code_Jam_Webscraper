import sys

DEBUG = True

def check_for_winner(line):
    line_type = 'T'
    for c in line:
        if c == '.':
            return None, True
        elif c == 'T':
            continue
        else:
            if line_type == 'T':
                line_type = c
            elif line_type != c:
                return None, False
    return line_type, False

def solver(board):
    has_empty = False
    winner = None
    # check all columns and rows for a winner
    for i in range(4):
        col = ''
        row = ''
        for j in range(4):
            col += board[j][i]
            row += board[i][j]
        winner, has_empty = check_for_winner(col)
        if winner:
            break
        winner, has_empty = check_for_winner(row)
        if winner:
            break
    # check diagonals
    if winner is None:
        diag1 = ""
        diag2 = ""
        for i in range(4):
            diag1 += board[i][i]
            diag2 += board[i][3-i]
        winner, has_empty = check_for_winner(diag1)
        if not winner:
            winner, has_empty = check_for_winner(diag2)
    if winner is not None:
        return '%s won' % winner
    elif has_empty:
        return 'Game has not completed'
    else:
        return 'Draw'

def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        board = []
        for i in range(4):
            board.append(rl().strip())
        rl()
        assert(len(board) == 4)
        for row in board:
            assert(len(row) == 4)
        answer = solver(board)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
