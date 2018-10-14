###
 # Uian Sol Gorgonio <sol.uian@gmail.com>
 # Apr 13 2013
 # Google Code Jam 2013 - Qualification Round
 # Problem A 
 ##/

def read_board():
    board = []
    for j in xrange(4):
        board.append(list(raw_input()))
    raw_input()
    return board 

def confere_linha(board, nTC):
    for i in xrange(4):
        if set(board[i]) == set(['X']) or set(board[i]) == set(['X', 'T']):
            print "Case #%d: X won" % nTC
            return True
        if set(board[i]) == set(['O']) or set(board[i]) == set(['O', 'T']):
            print "Case #%d: O won" % nTC
            return True
    return False

def confere_coluna(board, nTC):    
    for i in xrange(4):
        col = [board[0][i], board[1][i], board[2][i], board[3][i]]
        if set(col) == set(['X']) or set(col) == set(['X', 'T']):
            print "Case #%d: X won" % nTC
            return True
        if set(col) == set(['O']) or set(col) == set(['O', 'T']):
            print "Case #%d: O won" % nTC
            return True
    return False 

def confere_diag_princ(board, nTC):
    diag = [board[0][0], board[1][1], board[2][2], board[3][3]]
    if set(diag) == set(['X']) or set(diag) == set(['X', 'T']):
        print "Case #%d: X won" % nTC
        return True
    if set(diag) == set(['O']) or set(diag) == set(['O', 'T']):
        print "Case #%d: O won" % nTC
        return True
    return False

def confere_diag_sec(board, nTC):
    diag = [board[0][-1], board[1][-2], board[2][-3], board[3][-4]]
    if set(diag) == set(['X']) or set(diag) == set(['X', 'T']):
        print "Case #%d: X won" % nTC
        return True
    if set(diag) == set(['O']) or set(diag) == set(['O', 'T']):
        print "Case #%d: O won" % nTC
        return True
    return False

def confere_jogo_completo(board, nTC):
    for i in xrange(4):
        for j in xrange(4):
            if board[i][j] == '.':
                return False

    print "Case #%d: Draw" % nTC
    return True


# main
tc = int(raw_input())

for nTC in xrange(1, tc + 1):
    board = read_board()

    if (confere_linha(board, nTC)): continue
    elif (confere_coluna(board, nTC)): continue 
    elif (confere_diag_princ(board, nTC)): continue
    elif (confere_diag_sec(board, nTC)): continue
    elif (confere_jogo_completo(board, nTC)): continue
    else: print "Case #%d: Game has not completed" % nTC
