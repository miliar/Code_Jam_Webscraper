from sys import argv

def findstate(board):
    boardcolumn = []
    p = 0
    q = 0
    while q <= 3:
        boardcolumnrow = []
        while p<= 3:
            boardcolumnrow.append(board[p][q])
            #print board[p][q]
            p += 1
        boardcolumn.append(boardcolumnrow)
        p = 0
        q += 1     
    
###############################################################    
    for row in board:
        test = set(row)
        xwin = set(['X','T'])
        xwin2 = set(['X'])
        owin = set(['O','T'])
        owin2 = set(['O'])
        if test == xwin or test == xwin2:
            return "X won"
        if test == owin or test == owin2:
            return "O won"
    diagonal1 = []
    diagonal2 = []
    i = 0
    j = -1
    while i <= 3 and j>= -4:
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][j])
        i += 1
        j -= 1
    if set(diagonal1) == xwin or set(diagonal1) == xwin2:
        return "X won"
    if set(diagonal1) == owin or set(diagonal1) == owin2:
        return "O won"
    if set(diagonal2) == xwin or set(diagonal2) == xwin2:
        return "X won"
    if set(diagonal2) == owin or set(diagonal2) == owin2:
        return "O won"
################################################################    
    for row in boardcolumn:
        test = set(row)
        xwin = set(['X','T'])
        xwin2 = set(['X'])
        owin = set(['O','T'])
        owin2 = set(['O'])
        if test == xwin or test == xwin2:
            return "X won"
        if test == owin or test == owin2:
            return "O won"
    diagonal1 = []
    diagonal2 = []
    i = 0
    j = -1
    while i <= 3 and j>= -4:
        diagonal1.append(boardcolumn[i][i])
        diagonal2.append(boardcolumn[j][j])
        i += 1
        j -= 1
    if set(diagonal1) == xwin or set(diagonal1) == xwin2:
        return "X won"
    if set(diagonal1) == owin or set(diagonal1) == owin2:
        return "O won"
    if set(diagonal2) == xwin or set(diagonal2) == xwin2:
        return "X won"
    if set(diagonal2) == owin or set(diagonal2) == owin2:
        return "O won"
################WON Finished
    for row in board:
        if '.' in row:
            return "Game has not completed"
    return "Draw"
    
    
    
    
    
    return "Gbeke"

f =  open(argv[1], 'r')
T = eval(f.readline())
lines = f.readlines()
boardcontents = []

for word in lines:
    for letter in word:
        if letter == 'X' or letter == 'O' or letter == 'T' or letter == '.':
            #d = {'X':1, 'O':2, 'T':3, '.':4}
            boardcontents.append(letter)

count = 0
index = 1
while count < T*4:
    board = []
    i = 0
    while i <= 3:
        board.append(boardcontents[4*count : 4*count+4])
        i += 1
        count += 1
    state = findstate(board)
    
    print "Case #%d: %s" % (index, state)
    index += 1
