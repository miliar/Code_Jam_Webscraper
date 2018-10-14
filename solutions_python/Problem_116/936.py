import sys
import time
import itertools

xWinningState = map(''.join,[i for i in itertools.permutations('XXXT')])
xWinningState.append('XXXX')

oWinningState = map(''.join,[i for i in itertools.permutations('OOOT')])
oWinningState.append('OOOO')



def appendDiagonalElement(lists):
    #print lists
    d1=''.join([lists[i][i] for i in range(4)])
    d2=''.join([lists[3-i][i] for i in range(3,-1,-1)])
    lists.append(d1)
    lists.append(d2)
def appendColumnElement(lists):
    c1=''.join([lists[i][0] for i in range(4)])
    c2=''.join([lists[i][1] for i in range(4)])
    c3=''.join([lists[i][2] for i in range(4)])
    c4=''.join([lists[i][3] for i in range(4)])
    lists.append(c1)
    lists.append(c2)
    lists.append(c3)
    lists.append(c4)

def evaluateGameTable(lists):
    isRowEmpty = False
    #print lists
    for row in lists:
        if row in xWinningState:
            return 'X won'
        if row in oWinningState:
            return 'O won'
        if '.' in row:
            isRowEmpty = True
    if isRowEmpty:
        return 'Game has not completed'
    return 'Draw'
        
    

def evaluate(fileLocation):
    inputFile = open(fileLocation,'r')
    outputFile = open(fileLocation.replace('.in','.out'),'w')

    testCases = int(inputFile.readline())
    lineNumber = 1
    while 1:
        firstLine = inputFile.readline()

        if firstLine == '':
            inputFile.close()
            outputFile.close()
            return
        gameTable=list()

        gameTable.append(firstLine.rstrip())
        
        for i in range(3):
            gameTable.append(inputFile.readline().rstrip())

        appendDiagonalElement(gameTable)
        appendColumnElement(gameTable)
        
        state = evaluateGameTable(gameTable)
        outputFile.write('Case #%d: %s\n'%(lineNumber,state))
        lineNumber += 1
        inputFile.readline()


if __name__ == '__main__':
    startTime = time.time()
    evaluate(sys.argv[1])
    stopTime = time.time()
    print 'time required',stopTime-startTime
    
