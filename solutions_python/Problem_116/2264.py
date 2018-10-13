def checkRows(matrix):
    for row in matrix:
        numOfT = row.count("T")
        numOfX = row.count("X") + numOfT
        if numOfX > 3:
            return "X won"

        numOfO = row.count("O") + numOfT
        if numOfO > 3:
            return "O won"
        
    return "Draw"

def checkDiagonals(matrix):
    diag1, diag2 = getDiagonals(matrix)
    for row in [diag1, diag2]:
        numOfT = row.count("T")
        numOfX = row.count("X") + numOfT
        if numOfX > 3:
            return "X won"

        numOfO = row.count("O") + numOfT
        if numOfO > 3:
            return "O won"
        
    return "Draw"

def getDiagonals(matrix):
    diag1 = []
    diag2 = []
    for i,row in enumerate(matrix):
        diag1.append(row[i])
        diag2.append(row[-1*i - 1])
    
    return diag1, diag2


def checkForIncomplete(matrix):
    for row in matrix:
        numOfP = row.count(".")
        if numOfP > 0:
            return "Game has not completed"
        
    return "Draw"


def ticTacToe(inputText):
    outPut = open("output","w")
    inputText = open(inputText)
    numOfCases =  int(inputText.readline()[:-1])

    print numOfCases
    
    setOfMatrix = []
    for case in range(numOfCases):
        matrix = []
        for numOfRow in range(4):
            tempRow = inputText.readline()[:-1]
            row = [x for x in tempRow]
            matrix.append(row)
        
        #Check for a winner with rows
        winner = checkRows(matrix) 
        if winner == "Draw":
            #Check for a winner with columns
            transposed = zip(*matrix)
            winner = checkRows(transposed) 

        if winner == "Draw":
            #Check for a winner with diagonals
            winner = checkDiagonals(matrix) 

        if winner == "Draw":
            #Check for an incomplete game
            winner = checkForIncomplete(matrix) 
        
        outPut.write("Case #"+str(case + 1)+": " + winner + "\n")      
        
        # This is for the line between the cases
        tempRow = inputText.readline()[:-1]
        setOfMatrix.append(matrix)

    return setOfMatrix



if __name__ == "__main__":
    a = ticTacToe("A-large.in")
    #a = ticTacToe("A-large-practice.in")
    b, c = getDiagonals(a[1])
    print "DONE" 
