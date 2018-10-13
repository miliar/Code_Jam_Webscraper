import sys

fileIn = open('A-large.in', 'r')
fileOut = open('output.txt', 'w+')

testCases = int(fileIn.readline())


def lineStatus(line):
    ''' Returns the state of an individual line of characters. '''
    # Keep track of letter counts. 4 or 3+1T = a win
    if line.count('.') > 0:
        return None
    
    Xcount = line.count('X')
    Ocount = line.count('O')
    Tcount = line.count('T')

    if (Xcount == 4) or (Xcount == 3 and Tcount == 1):
        return 'X won'
    elif (Ocount == 4) or (Ocount == 3 and Tcount == 1):
        return 'O won'
    else:
        return None


def boardStatus(board):
    ''' Returns the state of the board after checking each row, column and diagonal. '''
    # Check rows:
    for row in range(0, 4):
        output = lineStatus(board[row])
        if output != None:
            return output

    # Check columns:
    for column in range(0, 4):
        col = [board[0][column],
               board[1][column],
               board[2][column],
               board[3][column]]
        output = lineStatus(col)
        if output != None:
            return output

    # Check top-left diagonal
    diagonal = [board[0][0],
                board[1][1],
                board[2][2],
                board[3][3]]
    output = lineStatus(diagonal)
    if output != None:
        return output

    # Check top-right diagonal
    diagonal = [board[0][3],
                board[1][2],
                board[2][1],
                board[3][0]]
    output = lineStatus(diagonal)
    if output != None:
        return output

    # Check for any dots. If > 0, Game not yet completed. Else Draw.
    for sublist in range(0, 4):
        if board[sublist].count('.') > 0:
            return 'Game has not completed'

    return 'Draw'


### MAIN PROGRAM ###
for case in range(0, testCases):
    board = [[],[],[],[]]
    for i in range(0, 4):
        board[i] = list(fileIn.readline().strip())

    output = boardStatus(board)

    fileOut.write('Case #'
                  + str(case + 1)
                  + ': '
                  + str(output)
                  + '\n')

    dummy = fileIn.readline() # Empty line after each case.

fileIn.close()
fileOut.close()
### END ###
