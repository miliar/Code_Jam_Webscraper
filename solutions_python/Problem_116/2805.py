N=int(raw_input())
def isOver(B):
    for i in xrange(4):
        for j in xrange(4):
            if B[i][j]=='.':
                return False
    return True
def outPut(B,P):
    Win=False
    for i in xrange(4):
        for j in xrange(4):
            if B[i][j]==P or B[i][j]=='T':
                if j==3:
                    return True
            else:
                break
    for i in xrange(4):
        for j in xrange(4):
            if B[j][i]==P or B[j][i]=='T':
                if j==3:
                    return True
            else:
                break
    for i in xrange(4):
        if B[i][i]==P or B[i][i]=='T':
            if i==3:
                return True
        else:
            break
    for i in xrange(4):
        if B[i][3-i]==P or B[i][3-i]=='T':
            if i==3:
                return True
        else:
            break            
    return Win
for i in xrange(N):
    Board=[]
    for j in xrange(4):
        Board.append(raw_input())
    raw_input()
    if outPut(Board,"X"):
        print "Case #"+str(i+1)+": X won"
    elif outPut(Board,"O"):
        print "Case #"+str(i+1)+": O won"
    elif isOver(Board):
        print "Case #"+str(i+1)+": Draw"
    else:
        print "Case #"+str(i+1)+": Game has not completed"
        
 
    

