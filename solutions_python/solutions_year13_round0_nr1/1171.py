#!/usr/bin/env python

T = long(raw_input())            #number of real tests
for t in range(1,T+1):
    A = []
    for i in range(4):
        x = raw_input()
        A.append([q for q in x])
    x = raw_input()  #get rid of trailing blank line
        
    out = ""
    dotcnt = 0
    #we have the board now look for winners
    for r in range(4):
        if A[r].count('X') + A[r].count('T') == 4:
            out = "X won"
        elif A[r].count('O') + A[r].count('T') == 4:
            out = "O won"
        dotcnt = dotcnt + A[r].count('.')
    if out:
        print "Case #%i: %s"%(t,out)
        continue
    
    C=[]    #check one diagonal
    for r in range(4):
        C.append(A[r][r])                   #build the diagonal
    if C.count('X') + C.count('T') == 4:
        out = "X won"
    elif C.count('O') + C.count('T') == 4:
        out = "O won"
    if out:
        print "Case #%i: %s"%(t,out)
        continue

    C=[]    #check other diagonal
    for r in range(4):
        c=3-r
        C.append(A[r][c])                   #build the diagonal
    if C.count('X') + C.count('T') == 4:
        out = "X won"
    elif C.count('O') + C.count('T') == 4:
        out = "O won"
    if out:
        print "Case #%i: %s"%(t,out)
        continue

    B = []
    x = []
    for c in range(4):
        for r in range(4):
            x.append(A[r][c])
        B.append(x)
        x=[]
    for r in range(4):
        if B[r].count('X') + B[r].count('T') == 4:
            out = "X won"
        elif B[r].count('O') + B[r].count('T') == 4:
            out = "O won"
    if out:
        print "Case #%i: %s"%(t,out)
        continue

    if dotcnt == 0:
        print "Case #%i: %s"%(t,"Draw")
    else:
        print "Case #%i: %s"%(t,"Game has not completed")
