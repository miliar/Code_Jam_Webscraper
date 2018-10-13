def convert(board, what):
    newboard = []
    for line in board:
        newline = []
        for char in line:
            if char == 'T':
                newline.append(what)
            else:
                newline.append(char)
        newboard.append(newline)
    return newboard

def check_for_victory(board, what):
    for x in board:
        points = 0
        for y in x:
            if y == what:
                points += 1
        if points == 4:
            return True
    for x in range(4):
        points = 0
        for y in range(4):
            if board[y][x] == what:
                points += 1
        if points == 4:
            return True
    if(board[0][0] == what and board[1][1] == what and board[2][2] == what
       and board[3][3] == what):
        return True
    if(board[0][3] == what and board[1][2] == what and board[2][1] == what
       and board[3][0] == what):
        return True
    return False

def check_for_draw(board):
    for x in board:
        for y in x:
            if y == '.':
                return False
    return True
                
target = open('A-large.in')
answer = open('A-large.txt', 'w')
target_string = target.read()
line = target_string.splitlines()
number_test_cases = int(line[0])
for case in range(number_test_cases):
    answer.write('Case #' + str(case+1) + ': ')
    board = line[1 + 5*(case):5 + 5*(case)]
    for x in range(len(board)):
        board[x] = list(board[x])
    boardX = convert(board, 'X')
    if check_for_victory(boardX, 'X'):
        answer.write('X won')
    elif check_for_victory(convert(board, 'O'), 'O'):
        answer.write('O won')
    elif check_for_draw(board):
        answer.write('Draw')
    else:
        answer.write('Game has not completed')
    answer.write('\n')

target.close()
answer.close()
