def tictac(board):
    """
    Case #1: X won
    Case #2: Draw
    Case #3: Game has not completed
    Case #4: O won

    diagonal : 0, 5, 10, 15
    diagonal : 03, 06, 09, 12
    vertical : V = V + 4*y
    horizonl : H = H + 4*x
    00 01 02 03
    04 05 06 07
    08 09 10 11
    12 13 14 15
    """

    horizonlSet = horizontal(board)
    verticalSet = vertaical(board)
    diagonalSet = diagonal(board)

    completeBoard = horizonlSet + verticalSet + diagonalSet

    for posibleSet in completeBoard:
        if posibleSet.count("x") + posibleSet.count("t") == 4:
            return "X won"
        elif posibleSet.count("o") + posibleSet.count("t") == 4:
            return "O won"
        else:
            pass

    if board.count(".") > 0:
        return "Game has not completed"
    else:
        return "Draw"

def diagonal(board):
    """
    return diagonal elements
    """
    diagonalSet = []
    x = [0,3]
    j = 0
    i = 0
    diagonalSet.append(board[0]+board[5]+board[10]+board[15])
    diagonalSet.append(board[3]+board[6]+board[9]+board[12])
    return diagonalSet

def horizontal(board):
    """
    return all possible horizontal elements
    """
    horizonlSet = []
    i = 0
    while i < 13:
        horiS = ""
        j = 0
        while j < 4:
            horiS += board[i + j]
            j += 1
        horizonlSet.append(horiS)
        i += 4
    return horizonlSet

def vertaical(board):
    """
    return all possible vertical elements
    """
    verticalSet = []
    i = 0

    while i < 4:
        veriS = ""
        j = 0
        while j < 4:
            veriS += board[i+j*4]
            j += 1
        verticalSet.append(veriS)
        i += 1
    return verticalSet

def main(inFile, outfile):
    """
    file read write function
    """
    cases = int(inFile.readline())
    cases += 1
    i = 1
    while i < cases:
        tiles = ""
        j = 0
        while j < 4:
            tiles += (inFile.readline().lower().split("\n")[0])
            j += 1
        inFile.readline()

        casecounter = tictac(tiles)
        outWrite = "Case #%d: %s\n" % (i, casecounter)
        outFile.write(outWrite)

        i += 1
    outFile.close()
    inFile.close()

if __name__ == "__main__":
    inFile = open("A.in", "r")
    outFile = open("A.out", "a")
    main(inFile, outFile)