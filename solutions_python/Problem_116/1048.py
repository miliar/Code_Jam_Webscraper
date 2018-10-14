from sys import stdin, stdout

def getResult(board):
    def isWinner(player):
        # search each row
        for row in range(0,4):
            count = 0
            for column in range(0,4):
                if board[row][column] is player or board[row][column] is 'T':
                    count+=1
            if count == 4:
                return True
        # search each column
        for column in range(0,4):
            count = 0
            for row in range(0,4):
                if board[row][column] is player or board[row][column] is 'T':
                    count+=1
            if count == 4:
                return True
        # search each diagonal
        count = 0
        for index in range(0,4):
            if board[index][index] is player or board[index][index] is 'T':
                count+=1
        if count == 4:
            return True
        
        count = 0
        for index in range(0,4):
            if board[index][3-index] is player or board[index][3-index] is 'T':
                count+=1
        if count == 4:
            return True

        # nothing found
        return False

    def isFull():
        for row in range(0,4):
            for column in range(0,4):
                if board[row][column] is '.':
                    return False
        return True
                
    if isWinner('X'):
        return "X won"
    elif isWinner('O'):
        return "O won"
    elif isFull():
        return "Draw"
    else:
        return "Game has not completed"

def main():
    testcases = int(stdin.readline())
    for testcase in range(1,testcases+1):
        if(testcase != 1):
            stdin.readline()
        board = []
        for i in range(4):
            board.append(stdin.readline())
        result = getResult(board)
        fstring = "Case #%d: %s" % (testcase,result)
        print fstring

if __name__ == "__main__":
    main()
