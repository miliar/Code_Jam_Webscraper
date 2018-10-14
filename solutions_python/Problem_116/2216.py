import sys

def main():
    filename = sys.argv[1]
    inputFile = open(filename+".in").read();
    outputFile = open(filename+ ".out", "w")
    lines = inputFile.splitlines()
    lines.reverse()
    testCases = lines.pop()

    for test in range(0, int(testCases)):
        board = []
        for row in range (0, 4):
            board.append(list(lines.pop()))
        if (len(lines) > 0):
            lines.pop() #empty row

        result = "Case #" + str(test+1) +": " + checkWinners(board) + "\n"
        outputFile.write(result)

def checkWinners(board):
    cols = {'X': [0]*4, 'O': [0]*4, 'T': [0]*4, '.': [0]*4}
    rows = {'X': [0]*4, 'O': [0]*4, 'T': [0]*4, '.': [0]*4}
    diags = {'X': [0]*7, 'O': [0]*7, 'T': [0]*7, '.': [0]*7}
    adiags = {'X': [0]*7, 'O': [0]*7, 'T': [0]*7, '.': [0]*7}

    xWon = False
    oWon = False

    numPeriods = 0

    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            piece = board[row][col]
            cols[piece][col]+= 1
            rows[piece][row]+= 1
            diags[piece][row-col + 3]+= 1
            adiags[piece][row+col]+= 1

            if (cols['X'][col] + cols['T'][col] == 4 or rows['X'][row] + rows['T'][row] == 4 or diags['X'][row-col+3] + diags['T'][row-col+3] == 4 or adiags['X'][row+col] + adiags['T'][row+col] == 4):
                xWon = True
            if (cols['O'][col] + cols['T'][col] == 4 or rows['O'][row] + rows['T'][row] == 4 or diags['O'][row-col+3] + diags['T'][row-col+3] == 4 or adiags['O'][row+col] + adiags['T'][row+col] == 4):
                oWon = True

            if (piece == '.'):
                numPeriods += 1

    if ((xWon and oWon) or not (xWon or oWon)):
        if (numPeriods == 0):
            return "Draw"
        else:
            return "Game has not completed"
    elif (xWon):
        return "X won"
    elif (oWon):
        return "O won"

    return "ERROR"

main()