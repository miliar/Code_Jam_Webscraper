import sys

def TicTacToe():   
    
    rx = list()
    ro = list()
    
    for j in range(0,4):
        rx.append(raw_input())
        ro.append(rx[j])
        rx[j] = rx[j].replace('T', 'X')
        ro[j] = ro[j].replace('T', 'O')
        
    cx = list()
    co = list()
    for j in range(0,4):
        cx.append(''.join(rx[0][j]+rx[1][j]+rx[2][j]+rx[3][j]))
        co.append(''.join(ro[0][j]+ro[1][j]+ro[2][j]+ro[3][j]))
        
    dx1 = ''.join(rx[0][0]+rx[1][1]+rx[2][2]+rx[3][3])
    do1 = ''.join(ro[0][0]+ro[1][1]+ro[2][2]+ro[3][3])
    dx2 = ''.join(rx[0][3]+rx[1][2]+rx[2][1]+rx[3][0])
    do2 = ''.join(ro[0][3]+ro[1][2]+ro[2][1]+ro[3][0])

    #debug code start
    """
    print "--------------DEBUG--------------"
    print ro
    print rx
    print co
    print cx
    print dx1
    print dx2
    print do1
    print do2
    print 
    print "--------------DEBUG--------------"
    """
    #debug code end

    #check for dots
    for j in range(0,4):
        max_dots = 0
        max_dots = max(max_dots, rx[j].count('.'))
        max_dots = max(max_dots, ro[j].count('.'))
        max_dots = max(max_dots, cx[j].count('.'))
        max_dots = max(max_dots, co[j].count('.'))
        
    max_dots = max(max_dots, dx1.count('.'))
    max_dots = max(max_dots, dx2.count('.'))
    max_dots = max(max_dots, do1.count('.'))
    max_dots = max(max_dots, do2.count('.'))
    #if (max_dots > 0):
    #    print "Case #"+str(i+1)+": Game has not completed"
    #check for X and O's
    max_X = 0
    for j in range(0,4):
        
        max_X = max(max_X, rx[j].count('X'))
        max_X = max(max_X, ro[j].count('X'))
        max_X = max(max_X, cx[j].count('X'))
        max_X = max(max_X, co[j].count('X'))
        
    max_X = max(max_X, dx1.count('X'))
    max_X = max(max_X, dx2.count('X'))
    max_X = max(max_X, do1.count('X'))
    max_X = max(max_X, do2.count('X'))
    if (max_X == 4):
        return ": X won"
    else:
        max_O = 0
        for j in range(0,4):                
            max_O = max(max_O, rx[j].count('O'))
            max_O = max(max_O, ro[j].count('O'))
            max_O = max(max_O, cx[j].count('O'))
            max_O = max(max_O, co[j].count('O'))
            
        max_O = max(max_O, dx1.count('O'))
        max_O = max(max_O, dx2.count('O'))
        max_O = max(max_O, do1.count('O'))
        max_O = max(max_O, do2.count('O'))
        if (max_O == 4):
            return ": O won"
        else:
            if (max_dots > 0):
                return ": Game has not completed"
            else:
                return ": Draw"
    



if __name__ == "__main__":
    testcases = int(raw_input())
    for i in range(0, testcases):
        print "Case #"+str(i+1)+TicTacToe();
        if (i != testcases-1):
            temp = raw_input()
