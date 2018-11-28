def checkHelper(s,O,X):
    if 'O' * 4 in s:
        O = True
    if 'O' * 3 in s and 'T' in s:
        O = True
    if 'X' * 4 in s:
        X = True
    if 'X' * 3 in s and 'T' in s:
        X = True
    return O,X

def check(board):
    print 'board '+str(board)
    n = len(board)
    numEmpties = 0
    O,X = False,False
#check rows and columns
    for i in range(n):
        s = ''.join(board[i])
        print 'row: '+s
        if '    .' in s:
            numEmpties += s.count('.')
            continue
        else:
            O,X = checkHelper(s,O,X)

        s = ''.join(board[j][i] for j in range(n))
        if '.' in s:
            numEmpties += s.count('.')
            continue
        else:
            O,X = checkHelper(s,O,X)

    for i in range(n):
        j = 0
        s = ''.join(board[i+d][j+d] for d in range(n-i))
        if '.' in s:
            numEmpties += s.count('.')
            continue
        else:
            O,X = checkHelper(s,O,X)
        
        s = ''.join(board[j+d][i-d] for d in range(i+1))
        if '.' in s:
            numEmpties += s.count('.')
            continue
        else:
            O,X = checkHelper(s,O,X)

    if O:
        return 'O won'
    elif X:
        return 'X won'
    elif numEmpties == 0:
        return 'Draw'
    else:
        return 'Game has not completed'


with open('TTTT-A-small-practice.in.txt') as f:
    content = f.read().splitlines()

numTests = int(content[0])
fileText = content[1:]
offset = 0
i=1
f = open ('TTTTSmalloutput.txt','w')
while i<=numTests:
    currBoard = []
    line = fileText[offset]
    boardSize = 0
    while len(line) > 0:
        boardSize += 1
#        if not '.' in line and not 'X' in line and not 'O' in line and not 'T' in line:
#            print 'broke'
#            break
        if (offset+boardSize) < len (fileText):
            line = fileText[offset+boardSize]
        else:
            break
    currBoard = fileText[offset:offset+boardSize]
    outputStr = check(currBoard)
    f.write('Case #'+str(i) + ': ' + outputStr+'\n')
    offset += boardSize + 1
    i+=1