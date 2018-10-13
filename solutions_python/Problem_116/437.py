def won(array, fields):
    #print "array:", array
    #print "[won]: checking:", fields
    result = False
    #check rows:
    for row in xrange(len(array)):
        ok = True
        #print array[row]
        for col in xrange(len(array[row])):
            if array[row][col] not in fields:
                ok = False
                break
        if ok:
            #print "found in rows:", row
            return True
    
    #check cols:
    for col in xrange(len(array[0])):
        ok = True
        for row in xrange(len(array)):
            if array[row][col] not in fields:
                ok = False
                break
        if ok:
            #print "found in cols:", col
            return True
    
    #check diagonals:
    ok = True
    for i in xrange(len(array)):
        #print i, i
        if array[i][i] not in fields:
            ok = False
    if ok:
        #print "found in diag1"
        return True
    
    ok = True
    for i in xrange(len(array)):
        #print (len(array)-1-i), i
        if array[len(array)-1-i][i] not in fields:
            ok = False
    if ok:
        #print "found in diag2"
        return True
    
    return False

def no_field(array, f):
    for row in xrange(len(array)):
        for col in xrange(len(array[row])):
            if array[row][col] == f:
                return False
    return True

import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    array = []
    for _ in xrange(4):
        l = sys.stdin.readline().strip()
        array.append(l)
    sys.stdin.readline()
    wonX = won(array, ['X', 'T'])
    wonO = won(array, ['O', 'T'])
    
    def result(wonX, wonY):
        if (wonX and wonY):
            return "Draw"
        elif wonX:
            return "X won"
        elif wonO:
            return "O won"
        elif no_field(array, '.'):
            return "Draw"
        else:
            return "Game has not completed"
    
    print "Case #"+str(case)+": "+result(wonX, wonO)
