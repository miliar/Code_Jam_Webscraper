DEBUG = False

def check_diagonal(x, data, char, reverse=False):
    if data[x] == '':
        return False
        
    if not reverse:
        if data[x][x] == 'T' or data[x][x] == char:
            if x == 3:
                return True
            x += 1
                
            return check_diagonal(x, data, char, reverse)
        
    else:
        if data[x][3 - x] == 'T' or data[x][3 - x] == char:
            if x == 0:
                return True
            x -= 1
            
            return check_diagonal(x, data, char, reverse)
        
    return False
    
def check_column(x, y, data, char):
    for column in range(4):
        if not data[column][y] == 'T' and not data[column][y] == char:
            return False
    return True
    
def check_row(x, y, data, char):
    for row in range(4):
        if not data[x][row] == 'T' and not data[x][row] == char:
            return False
    return True

def process_data(data, case_number, f_out):
    if DEBUG:
        print 'case #%s' % (case_number + 1)
    else:
        f_out.write('Case #%s: ' % (case_number + 1))
    
    complete = True
    x_win = False
    o_win = False
    
    for x in range(4):
        for y in range(4):
            if check_row(x, y, data, 'X') or check_column(x, y, data, 'X'):
                x_win = True
            if check_row(x, y, data, 'O') or check_column(x, y, data, 'O'):
                o_win = True
            if data[x][y] == '.':
                complete = False
    
    if check_diagonal(0, data, 'X') or check_diagonal(3, data, 'X', True):
        x_win = True
        
    if check_diagonal(0, data, 'O') or check_diagonal(3, data, 'O', True):
        o_win = True
        
    if DEBUG:
        if x_win and o_win:
            print 'Draw'
        elif x_win:
            print 'X won'
        elif o_win:
            print 'O won'
        else:
            if complete:
                print 'Draw'
            else:
                print 'Game has not completed'
    else:
        if x_win and o_win:
            f_out.write('Draw\n')
        elif x_win:
            f_out.write('X won\n')
        elif o_win:
            f_out.write('O won\n')
        else:
            if complete:
                f_out.write('Draw\n')
            else:
                f_out.write('Game has not completed\n')
    return
    
loc_in = r'c:\coding\codejam\problemA\data.in'
loc_out = r'c:\coding\codejam\problemA\data.out'
    
with open(loc_in, 'rb') as f_in:
    with open(loc_out, 'wb') as f_out:
        num_of_cases = f_in.next()
        
        for case_number in xrange(int(num_of_cases)):
            try:
                data = []
                for x in range(4):
                    data.append(f_in.next().strip('\n'))
                process_data(data, case_number, f_out)
                f_in.next()
            except StopIteration:
                break