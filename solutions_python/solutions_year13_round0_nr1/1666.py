import string

def ticTacToe(board):
    sz = 4
    cl1 = ''
    cl2 = ''
    cl3 = ''
    cl4 = ''
    dg1 = ''
    dg2 = ''
    cDot = 0
    for k in range(sz):
        oneRow = board[k]
        oneRow = oneRow.lower()

        cl1 = cl1+oneRow[0]
        cl2 = cl2+oneRow[1]
        cl3 = cl3+oneRow[2]
        cl4 = cl4+oneRow[3]
        dg1 = dg1 + oneRow[k]
        dg2 = dg2 + oneRow[3-k]
        cDot += oneRow.count('.')
        
        if oneRow.count('x') == sz:
            
            return 'X won'
        elif oneRow.count('x') == sz-1 and oneRow.count('t') == 1:
        
            return 'X won'
        elif oneRow.count('o') == sz:
            return 'O won'
        elif oneRow.count('o') == sz-1 and oneRow.count('t') == 1:
            return 'O won'
        
    clBoard = [cl1,cl2,cl3,cl4,dg1,dg2]
    for k in range(sz+2):
        oneRow = clBoard[k]
        
        if oneRow.count('x') == sz:
            return 'X won'
        elif oneRow.count('x') == sz-1 and oneRow.count('t') == 1:
            return 'X won'
        elif oneRow.count('o') == sz:
            return 'O won'
        elif oneRow.count('o') == sz-1 and oneRow.count('t') == 1:
            return 'O won'

    if cDot == 0:
        return 'Draw'
    else:
        return 'Game has not completed'




inFile = open('A-large.in','r')
outPut = open('tic_tac_toe2.in','w')
inPut = inFile.read()
inPut = inPut.split('\n')
T = int(inPut[0])
    
Cases = inPut[1:]
emt = Cases.count('')
for h in range(emt):
    Cases.remove('')
    
szz = len(Cases)
for k in range(1,szz/4+1):
    OutPut = ticTacToe(Cases[4*(k-1):4*k])
    outPut.write('Case #%d:' % (k) + " "+OutPut+'\n')
        
inFile.close()
outPut.close()
        
