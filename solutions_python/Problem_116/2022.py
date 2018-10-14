import sys

_boards = []
_winning_boards = [[[1,1,1,1],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]],
                   [[0,0,0,0],
                    [1,1,1,1],
                    [0,0,0,0],
                    [0,0,0,0]],
                   [[0,0,0,0],
                    [0,0,0,0],
                    [1,1,1,1],
                    [0,0,0,0]],
                   [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [1,1,1,1]],
                   [[1,0,0,0],
                    [1,0,0,0],
                    [1,0,0,0],
                    [1,0,0,0]],
                   [[0,1,0,0],
                    [0,1,0,0],
                    [0,1,0,0],
                    [0,1,0,0]],
                   [[0,0,1,0],
                    [0,0,1,0],
                    [0,0,1,0],
                    [0,0,1,0]],
                   [[0,0,0,1],
                    [0,0,0,1],
                    [0,0,0,1],
                    [0,0,0,1]],
                   [[1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]],
                   [[0,0,0,1],
                    [0,0,1,0],
                    [0,1,0,0],
                    [1,0,0,0]]]

def process_input(inputFile):
    global _boards

    f = open(inputFile, 'r')
    numCases = int(f.readline())
    
    if numCases < 1 or numCases > 1000:
        return False
    
    for x in range(numCases):
        board = []
        for y in range(4):
            board.append(f.readline().strip())
        _boards.append(board)
        f.readline() # empty line

    f.close()
    return True

def process_boards():
    global _boards
    
    caseNum = 1
    for board in _boards:
        sys.stdout.write("Case #%d: " % caseNum)
        process_board(board, caseNum)
        caseNum+=1

def process_board(board, caseNum):
    if check_for_winner(board, 'X'):
        sys.stdout.write("X won\n")
    elif check_for_winner(board, 'O'):
        sys.stdout.write("O won\n")
    elif not check_completed(board):
        sys.stdout.write("Game has not completed\n")
    else:
        sys.stdout.write("Draw\n")

def check_for_winner(board, playerChar):
    for winningBoard in _winning_boards:
        boardTest = [[0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]]

        for y in range(4):
            for x in range(4):
                if board[x][y] == playerChar or board[x][y] == 'T':
                    boardTest[x][y] = 1

        for y in range(4):
            for x in range(4):
                boardTest[x][y] = boardTest[x][y] and winningBoard[x][y]

        if boardTest == winningBoard:
            return True

    return False
            
def check_completed(board):
    for y in range(4):
        for x in range(4):
            if board[x][y] == '.':
                return False
    return True

if __name__ == "__main__":
    inputFile = sys.argv[1]
    
    if not process_input(inputFile):
        print "Error"

    process_boards()


    
