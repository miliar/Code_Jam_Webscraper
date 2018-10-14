board=[[] for k in xrange(4)]
xWin=False
oWin=False
empty=False


def boardCheck(board,case,outFile):
    global xWin, oWin,empty
    #print xWin, oWin, draw
    for i in xrange(4):
        winnerRow=retStat(i,"row")
        winnerCol=retStat(i,"column")
        
        if winnerRow=="X" or winnerCol=="X":
            xWin=True
            outFile.write("Case #%d: X won\n"%case)
            break
        elif winnerRow=="O" or winnerCol=="O":
            oWin=True
            outFile.write("Case #%d: O won\n"%case)
            break
    winnerMDiag=retStat(0,"mdiagonal")
    winnerSDiag=retStat(0,"sdiagonal")
        
    
    
    if xWin==False and oWin==False:
        if winnerMDiag=="X" or winnerSDiag=="X":
            xWin=True
            outFile.write("Case #%d: X won\n"%case)
        elif winnerMDiag=="O" or winnerSDiag=="O":
            oWin=True
            outFile.write("Case #%d: O won\n"%case)
            
        elif empty==True:
            outFile.write("Case #%d: Game has not completed\n"%case)
        else:
            outFile.write("Case #%d: Draw\n"%case)

    
def inputHandler1(filename):
    global board,xWin,oWin,empty
    outFile=open("output4.txt","w")
    counter=case=0
    i=1
    inFile=open(filename,"r")
    lines=inFile.readlines()
    #print lines
    testCases=int(lines[0][:-1])
    if testCases!=0:
        while i<len(lines):
            if lines[i]=='\n':
                case+=1
                #print case
                boardCheck(board,case,outFile)
                board=[[] for k in xrange(4)]
                counter=-1
                oWin=xWin=False
                empty=False
            else:
                for char in lines[i]:
                    #print i,char
                    if char!='\n':
                        if char=='.':
                            empty=True
                        board[counter]+=[char]
            #print board
            
            i+=1
            counter+=1
        #boardCheck(board,case+1,outFile)
        outFile.close()

def retStat(index,mode):
    #print index,mode
    i=j=X=O=T=0
    if mode=="row":
        i=index
    elif mode=="column":
        j=index
    elif mode=="sdiagonal":
        j=4-i-1
        
    while i<len(board) and j<len(board):
        if board[i][j]=='X':
            X+=1
        elif board[i][j]=='O':
            O+=1
        elif board[i][j]=='T':
            T+=1
        if mode=="row":
            j+=1
        elif mode=="column":
            i+=1
        elif mode=="sdiagonal":
            i+=1
            j=4-i-1
        elif mode=="mdiagonal":
            i+=1
            j+=1
        
    #print mode,X,O,T
    if X+T==4:
        return 'X'
    elif O+T==4:
        return 'O'
    
inputHandler1("A-large.in")

