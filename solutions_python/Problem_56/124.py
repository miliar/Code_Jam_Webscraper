def read_board(size):
    lines = []
    for i in xrange(size):
        line = list(raw_input())
        lines.append(line)
        
    return lines

def rotate_and_fall(lines):
    new_matrix = []
    
    for line in lines:
        after_fall = [piece for piece in line if piece != '.']
        num_dots = len(line) - len(after_fall)
        
        new_line = list('.' *num_dots) + after_fall
        
        new_matrix.append(new_line)
        
    return new_matrix

def check_line_winner_in_pos(lines, k, i,j):
    # check line
    for n in xrange(k):
        if (i - n < 0) or (lines[i-n][j] != lines[i][j]):
            break
    else:
        return lines[i][j]
    
    return None

def check_diag1_winner_in_pos(lines, k, i,j):
    # check line
    for n in xrange(k):
        if (i - n < 0) or (j - n < 0) or (lines[i-n][j-n] != lines[i][j]):
            break
    else:
        return lines[i][j]
    
    return None

def check_diag2_winner_in_pos(lines, k, i,j):
    # check line
    for n in xrange(k):
        if (i - n < 0) or (j + n >= len(lines)) or (lines[i-n][j+n] != lines[i][j]):
            break
    else:
        return lines[i][j]
    
    return None

    
def check_column_winner_in_pos(lines, k, i,j):
    for n in xrange(k):
        if (j - n < 0) or (lines[i][j-n] != lines[i][j]):
            break
    else:
        return lines[i][j]
    
    return None

def add_winner(l, winner):
    if winner != '.' and winner != None:
        l.append(winner)
        
    return l

def check_winners(lines, k):
    winners = []
    for i in xrange(len(lines)):
        for j in xrange(len(lines)):
            winner_line = check_line_winner_in_pos(lines,  k, i, j)
            winner_column = check_column_winner_in_pos(lines,  k, i, j)
            winner_diag1 = check_diag1_winner_in_pos(lines,  k, i, j)
            winner_diag2 = check_diag2_winner_in_pos(lines,  k, i, j)
            

            add_winner(winners, winner_line)    
            add_winner(winners, winner_column)
            add_winner(winners, winner_diag1)
            add_winner(winners, winner_diag2)
            
    return winners
        
##def rotate(lines):
##    rotated = zip(*lines[::-1])
##    return rotated
##
##def fall(lines):
##    for column in xrange(len(lines)):
##        pieces = [line[column] for line in lines if line[column] != '.']
##        dots = 
##        pass


#print rotate_and_fall(read_board(3))
#print rotate([['1','.','3'], ['4','.','6'], ['.','8','.']])
#print fall([['.','4','1'], ['8','.','.'], ['.','6','3']])
#print rotate_and_fall([['1','.','3'], ['4','.','6'], ['.','8','.']])
##print check_winners([['.', '.', 'B'], 
##                     ['.', 'R', 'B'],
##                     ['.', 'R', 'B']],
##                    3)

##print check_winners(rotate_and_fall(
##                    [['.', '.', '.', '.', '.', '.',], 
##                    ['.', '.', '.', '.', '.', '.',],
##                    ['.', 'R', '.', '.', '.', 'R',],
##                    ['.', 'R', '.', '.', 'B', 'B',],
##                    ['.', 'R', '.', 'R', 'B', 'R',],
##                    ['R', 'B', '.', 'B', 'B', 'B']]),
##                    4)


def calculate(board, k):
    winners = check_winners(rotate_and_fall(board), k)
    
    if ('R' in winners) and ('B' in winners):
        return 'Both'
    
    if ('R' in winners):
        return 'Red'
    
    if ('B' in winners):
        return 'Blue'
    
    return 'Neither'
    
    
for case_number in xrange(int(raw_input())):
    n, k = map(int, raw_input().split())
    board = read_board(n)
    result = calculate(board, k)
    print 'Case #%d: %s' % (case_number+1, result)