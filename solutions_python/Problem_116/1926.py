num_test_cases = 0

def read_input(inputfile):
    handle = open(inputfile, 'r')
    num_test_cases = int(handle.readline())
    test_cases = []
    for i in xrange(num_test_cases):
        case = []
        for i in xrange(4):
            case.append(handle.readline().strip())
        handle.readline()
        test_cases.append(case)
    return test_cases

def check_horizontal(case):
    for row in case:
        if row.count('X') == 4 or (row.count('X') == 3 and row.count('T') == 1):
            return 'X'
        if row.count('O') == 4 or (row.count('O') == 3 and row.count('T') == 1):
            return 'O'
    return '-'

def check_vertical(case):
    for i in range(4):
        column = ''
        for j in range(4):
            column += case[j][i]
        if column.count('X') == 4 or (column.count('X') == 3 and column.count('T') == 1):
            return 'X'
        if column.count('O') == 4 or (column.count('O') == 3 and column.count('T') == 1):
            return 'O'
    return '-'

def check_left_diagonal(case):
    diagonal = ''
    for i in range(4):
        diagonal += case[i][i]
        if diagonal.count('X') == 4 or (diagonal.count('X') == 3 and diagonal.count('T') == 1):
            return 'X'
        if diagonal.count('O') == 4 or (diagonal.count('O') == 3 and diagonal.count('T') == 1):
            return 'O'
    return '-' 

def check_right_diagonal(case):
    diagonal = case[0][3] + case[1][2] + case[2][1] + case[3][0]
    if diagonal.count('X') == 4 or (diagonal.count('X') == 3 and diagonal.count('T') == 1):
        return 'X'
    if diagonal.count('O') == 4 or (diagonal.count('O') == 3 and diagonal.count('T') == 1):
        return 'O'
    return '-'

def check_draw(case):
    # call only after checking whether someone has won
    for i in case:
        if i.count('.') > 0:
            return False
    return True

def check_winner(case):
    winner = check_horizontal(case)
    if winner != '-':
        return winner
    winner = check_vertical(case)
    if winner != '-':
        return winner
    winner = check_left_diagonal(case)
    if winner != '-':
        return winner
    return check_right_diagonal(case)
    
        
test_cases = read_input('A-large.in')
for i in range(len(test_cases)):
    case = test_cases[i]
    output = 'Case #' + str(i + 1) + ': '
    winner = check_winner(case)
    if winner != '-':
        output += winner + ' won'
    else:
        if check_draw(case):
            output += 'Draw'
        else:
            output += 'Game has not completed'
    print output