def is_winning_line(line):
    winner = line[0]
    for i in xrange(4):
        if winner == 'T':
            winner = line[i]
        if line[i] == 'T':
            continue
        if line[i] == '.' or line[i] != winner:
            return False
    return True

def complete(board):
    for i in xrange(4):
        for j in xrange(4):
            if board[i][j] == '.':
                return False
    return True

def winner_of(line):
    # there can only be one T
    if line[0] == 'T':
        return line[1]
    return line[0]

def tic_easier(board):
    # List of lines (horizontals/verticals/diagonal) where we can win
    lines = board # horizontals
    # verticals
    lines += [[l[i] for l in board] for i in xrange(4)]
    # diagonals
    lines.append([board[i][i] for i in xrange(4)])
    lines.append([board[i][3-i] for i in xrange(4)])
    # winning lines
    win = filter(is_winning_line, lines)
    if win == []:
        if complete(board):
            return 'Draw'
        else:
            return 'Game has not completed'
    return '{} won'.format(winner_of(win[0]))
    
if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        board = [list(raw_input()) for _ in xrange(4)]
        print('Case #{}: {}'.format(i+1, tic_easier(board)))
        try:
            raw_input()
        except:
            pass
