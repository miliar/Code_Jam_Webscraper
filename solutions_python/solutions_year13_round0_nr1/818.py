# tic_tac_toe_tomek.py
#
# For Google Code Jam 2013
# David Lister
#


# Functions


def check_list(lst):
    '''
    Returns 'X' if X has won
    Returns 'O' if O has won
    Returns False if there are no wins
    '''
    
    if '.' in lst:
        return False
    
    x = lst.count('X')
    
    if x == 4:
        return 'X'
    
    elif x == 3:
        if lst.count('T'):
            return 'X'
        
        return False
    
    elif x > 0:
        return False

    o = lst.count('O')

    if o == 4:
        return 'O'

    elif o == 3:
        if lst.count('T'):
            return 'O'
    return False    

def vertical_check(game):
    '''
    Returns 'X' if X has a vertical line
    Returns 'O' if O has a vertical line
    Returns False if there are no vertical lines
    '''
    x = 0
    over = False
    while not over:
        test = [game[0][x], game[1][x], game[2][x], game[3][x]]
        over = check_list(test)
        x += 1
        if x == 4:
            break
            
    return over



def horizontal_check(game):
    '''
    Returns 'X' if X has a horizontal line
    Returns 'O' if O has a horizontal line
    Returns False if there are no horizontal lines
    '''
##    print game
    x = 0
    over = False
    while not over:
##        print x
        over = check_list(game[x])
        x += 1
        if x == 4:
            break
        
    return over


def diagonal_check(game):
    '''
    Returns 'X' if X has a diagonal line
    Returns 'O' if O has a diagonal line
    Returns False if there are no diagonal lines
    '''
    test = [game[0][0], game[1][1], game[2][2], game[3][3]]
    check = check_list(test)
    if check:
        return check

    test = [game[3][0], game[2][1], game[1][2], game[0][3]]
    check = check_list(test)
    return check

def draw_check(game):
    '''
    Return True if there is no winner, False otherrwise
    '''
    for row in game:
        for item in row:
            if item == '.':
                return False
            
    return True  # Alright... We'll call it a draw
                
        
        
fname = raw_input('Please enter file name: ')
fout = str(fname.split('.')[0]) + '.txt'

f = list(open(fname, 'r'))

games = []
temp = []
i = 1
p = 0
over = False
while not over:
    if p != 4:
        temp.append(list(f[i][:-1]))
        p += 1
    else:
        p = 0
        games.append(temp)
        temp = []

    i += 1

    if i == len(f):
        over = True

output = ''
i = 1
for game in games:
    win = horizontal_check(game)
    if win:
        output = output + 'Case #' + str(i) + ': ' + str(win) + ' won\n'
        
    else:        
        win = diagonal_check(game)
        if win:
            output = output + 'Case #' + str(i) + ': ' + str(win) + ' won\n'
            
        else:
            win = vertical_check(game)
            if win:
                output = output + 'Case #' + str(i) + ': ' + str(win) + ' won\n'
                
            elif draw_check(game):
                output = output + 'Case #' + str(i) + ': Draw\n'

            else:
                output = output + 'Case #' + str(i) + ': Game has not completed\n'
    i += 1

out = open(fout, 'w')
out.write(output)
out.close()

print output


