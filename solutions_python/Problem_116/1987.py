#the solution for problem A Tic-Tac-Toe-Tomek of google code jam 2013

def get_result(board):
    ''' (list(list)) -> (str)
    >>> get_result([['X', 'X', 'X', 'T'], ['.', '.', '.', '.'], ['O', 'O', '.', '.'], ['.', '.', '.', '.']])
    'X won'
    '''

    can_be_draw = True 
    #test for rows 
    for i in range(4):
        count_X = 0
        count_O = 0
        for j in range(4):
            if board[i][j] == 'X':
                count_X += 1
            elif board[i][j] == 'O':
                count_O +=1
            elif board[i][j] == 'T':
                count_X +=1
                count_O +=1
            else:
                can_be_draw = False
        if count_X == 4:
            return 'X won'
        elif count_O == 4:
            return 'O won'
            
    #test for coloums         
    for j in range(4):
        count_X = 0
        count_O = 0
        for i in range(4):
            if board[i][j] == 'X':
                count_X += 1
            elif board[i][j] == 'O':
                count_O +=1
            elif board[i][j] == 'T':
                count_X +=1
                count_O +=1
            else:
                can_be_draw = False
        if count_X == 4:
            return 'X won'
        elif count_O == 4:
            return 'O won'
            
    count_X = 0
    count_O = 0
    for i in range(4):
        j = i       
        if board[i][j] == 'X':
            count_X += 1
        elif board[i][j] == 'O':
            count_O +=1
        elif board[i][j] == 'T':
            count_X +=1
            count_O +=1
        else:
            can_be_draw = False
    if count_X == 4:
        return 'X won'
    elif count_O == 4:
        return 'O won'
           

    count_X = 0
    count_O = 0
    for i in range(4):
        j = 3 - i       
        if board[i][j] == 'X':
            count_X += 1
        elif board[i][j] == 'O':
            count_O +=1
        elif board[i][j] == 'T':
            count_X +=1
            count_O +=1
        else:
            can_be_draw = False
    if count_X == 4:
        return 'X won'
    elif count_O == 4:
        return 'O won'
           
    if can_be_draw:
        return 'Draw'
    else:
        return 'Game has not completed'

def get_board(str_board):
    '''(list(str)) -> (list(list))
    >>> get_board(['XXXT','....','OO..','....'])
    [['X', 'X', 'X', 'T'], ['.', '.', '.', '.'], ['O', 'O', '.', '.'], ['.', '.', '.', '.']]
    '''
    board = []
    for string in str_board:
        board = board + [list(string)]
    return board

#import doctest
#doctest.testmod()

T = int(raw_input())

for i in range(T):
    board_list = []
    for j in range(4):
        row = raw_input()
        board_list += [row]
    board = get_board(board_list)
    result = get_result(board)
    print 'Case #%d: %s' %(i+1, result)
    if i != (T-1):
        new_line = raw_input()
   # try:
   #     new_line = raw_input() #handles the new line after everytest case
   # except:
   #     error = 'Programme ended'
