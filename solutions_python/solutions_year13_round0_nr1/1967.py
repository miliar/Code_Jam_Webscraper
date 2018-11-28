solutions = [
  [ 0,  1,  2,  3], 
  [ 4,  5,  6,  7],
  [ 8,  9, 10, 11],
  [12, 13, 14, 15],
  [ 0,  4,  8, 12],
  [ 1,  5,  9, 13],
  [ 2,  6, 10, 14],
  [ 3,  7, 11, 15],
  [ 0,  5, 10, 15],
  [ 3,  6,  9, 12]
]

file = open('A-large.in', 'r')

def checkWin(line, char, board):
    count = 0
    for index in line:
        if board[index] == char or board[index] == "T":
            count += 1
    return count == 4

def doEverything(input, gameNum):
    board = []
    isFinished = True
    for value in input:
        for char in value:
            if char == ".":
                isFinished = False
            if char != "\n":
                board.append(char)

    xWin = False
    yWin = False
    for solution in solutions:
        if not xWin and checkWin(solution, 'X', board):
            xWin = True
        elif not yWin and checkWin(solution, 'O', board):
            yWin = True
        if xWin and yWin:
            break

    if xWin:
        print "Case #" + str(gameNum+1) + ": X won"
    elif yWin:
        print "Case #" + str(gameNum+1) + ": O won"
    elif isFinished:
        print "Case #" + str(gameNum+1) + ": Draw"
    else:
        print "Case #" + str(gameNum+1) + ": Game has not completed"
    

def main():
    readFile = file.readlines()
    numInputs = int(readFile[0].strip())

    for i in range(numInputs):
        doEverything(readFile[1+i*4+i : 4+i*4+1+i], i)
    #readIn(readFile[2:22]) # CHANGE THIS TO THE RIGHT NUMBER 




main()
