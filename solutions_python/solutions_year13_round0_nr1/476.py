import sys
from collections import defaultdict

def Owin(A):
    #check for diagonal
    Ocount = 0
    Tcount = 0
    for i in range(4):
        if A[i][i] == 'O': Ocount+=1
        elif A[i][i] == 'T': Tcount+=1
    if Ocount==4 or (Ocount==3 and Tcount==1):
        return True
    Ocount = 0
    Tcount = 0
    for i in range(4):
        if A[i][4-i-1] == 'O': Ocount+=1
        elif A[i][4-i-1] == 'T': Tcount+=1
    if Ocount==4 or (Ocount==3 and Tcount==1):
        return True

    #check left to right
    for i in range(4):
        Ocount = 0
        Tcount = 0
        for j in range(4):
            if A[i][j]=='O': Ocount+=1
            elif A[i][j]=='T': Tcount+=1
        if Ocount==4 or (Ocount==3 and Tcount==1):
            return True

    #check top to bottom
    for i in range(4):
        Ocount = 0
        Tcount = 0
        for j in range(4):
            if A[j][i]=='O': Ocount+=1
            if A[j][i]=='T': Tcount+=1
        if Ocount==4 or (Ocount==3 and Tcount==1):
            return True

def Xwin(A):
    #check for diagonal
    Ocount = 0
    Tcount = 0
    for i in range(4):
        if A[i][i] == 'X': Ocount+=1
        elif A[i][i] == 'T': Tcount+=1
    if Ocount==4 or (Ocount==3 and Tcount==1):
        return True
    Ocount = 0
    Tcount = 0
    for i in range(4):
        if A[i][4-i-1] == 'X': Ocount+=1
        elif A[i][4-i-1] == 'T': Tcount+=1
    if Ocount==4 or (Ocount==3 and Tcount==1):
        return True

    #check left to right
    for i in range(4):
        Ocount = 0
        Tcount = 0
        for j in range(4):
            if A[i][j]=='X': Ocount+=1
            elif A[i][j]=='T': Tcount+=1
        if Ocount==4 or (Ocount==3 and Tcount==1):
            return True

    #check top to bottom
    for i in range(4):
        Ocount = 0
        Tcount = 0
        for j in range(4):
            if A[j][i]=='X': Ocount+=1
            if A[j][i]=='T': Tcount+=1
        if Ocount==4 or (Ocount==3 and Tcount==1):
            return True

def emptySpace(A):
    for i in range(4):
        for j in range(4):
            if A[i][j] == '.':
                return True

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('jamqual1.out', 'w')
    t = int(f.readline())
    for test in range(1, t+1):
        str1 = "Case #%d: " % (test)
        output.write(str1)
        table = []
        for i in range(4):
            table.append(f.readline().strip())
        print table
        O_Win = Owin(table)
        X_Win = Xwin(table)
        empty = emptySpace(table)
        if (O_Win and X_Win) or (not O_Win and not X_Win and not empty):
            ans = 'Draw'
        elif O_Win and not X_Win:
            ans = 'O won'
        elif not O_Win and X_Win:
            ans = 'X won'
        else:
            ans = 'Game has not completed'
        output.write(ans+'\n')
        if test<t:
            #print 'yes'
            f.readline()    
    output.close()
        
        
        
