'''
Created on 13/04/13
Code Jam 2013 Qualification Round A
@author: manolo
'''

import sys
ifile = sys.stdin
def r():
    return ifile.readline()[:-1]

ofile = open('./a-large.out', 'w')
def w(what):
    ofile.write(what + '\n')

def check_line(l):

#    print "checking line " + str(l)
    x_wins = True
    o_wins = True
    for c in l:
#        print "c = " + str(c)
        if c == '.':
#            print 'line: ' + str(l) + ' --> not completed'
            return '.'
        x_wins = x_wins and (c == 'X' or c == 'T')
        o_wins = o_wins and (c == 'O' or c == 'T')
#        print "x_wins: " + str(x_wins)
#        print "o_wins: " + str(o_wins)

    if x_wins and o_wins:
#        print "X and O win, not possible"
        raise
    if x_wins:
#        print 'line: ' + str(l) + ' --> X wins'
        return 'X'
    if o_wins:
#        print 'line: ' + str(l) + ' --> O wins'
        return 'O'
        

t = int(r())

for c in range(1, t+1):
    line =[None] * 4
    someone_won = False
    game_not_completed = False
    
    # check rows
#    print str(c) + ":"
    for i in range(4):
        line[i] = list(r())
#        print line[i]
#    print
    
    for i in range(4):
#        print "line: " + str(line[i])
        res =check_line(line[i])
        if res == 'X':
            w('Case #' + str(c) + ': X won')
            someone_won = True
            break
        if res == 'O':
            w('Case #' + str(c) + ': O won')
            someone_won = True
            break
        if res == '.':
            game_not_completed = True
#    print ' '
    
    if not someone_won:
        # check cols
        for i in range(4):
            col = [line[0][i], line[1][i], line[2][i], line[3][i]]
            res=check_line(col)
            if res == 'X':
                w('Case #' + str(c) + ': X won')
                someone_won = True
                break
            if res == 'O':
                w('Case #' + str(c) + ': O won')
                someone_won = True
                break
            if res == '.':
                game_not_completed = True

#    print
    if not someone_won:
        # check diags
        diag1 = [line[0][0], line[1][1], line[2][2], line[3][3]]
        res=check_line(diag1)
        if res == 'X':
            w('Case #' + str(c) + ': X won')
            someone_won = True
        if res == 'O':
            w('Case #' + str(c) + ': O won')
            someone_won = True
        if res == '.':
            game_not_completed = True
    if not someone_won:    
        diag2 = [line[0][3], line[1][2], line[2][1], line[3][0]]
        res=check_line(diag2)
        if res == 'X':
            w('Case #' + str(c) + ': X won')
            someone_won = True
        if res == 'O':
            w('Case #' + str(c) + ': O won')
            someone_won = True
        if res == '.':
                game_not_completed = True

    if not someone_won:
        if game_not_completed:
#            print 'Case #' + str(c) + ': Game has not completed'
            w('Case #' + str(c) + ': Game has not completed')
        else:
#            print 'Case #' + str(c) + ': Draw'
            w('Case #' + str(c) + ': Draw')
        
    trash = r()


ofile.close

