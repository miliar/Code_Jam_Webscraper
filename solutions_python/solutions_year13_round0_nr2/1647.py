# make a board from some strings.

def col(matrix, i):
    return [row[i] for row in matrix]


def checkBoard( N, M, board ):
    nMax = []
    mMax = []



    for i in range(0,M):
        mMax.append(max(col(board,i)))

    for row in board:
        nMax.append(max(row))

    # for each cell, check that the height is the min of mMax and nMax.
    for x in range(0,N):
        for y in range(0,M):
            minHeight = min( [nMax[x], mMax[y]] )
            if ( board[x][y] != minHeight ):
                return "NO"
    return "YES"



testBoard = [[1,1,1],[2,2,1],[2,2,1]]
board = testBoard
N = 3
M = 3


        
print(checkBoard(N,M,board))

# Read from the input file.
filename = "test.txt"

file = open(filename,'r')

numTests = int(file.readline())

for i in range(0, numTests):
    # read the number N and M
    line = file.readline().replace("\n","").split(" ")
    N = int(line[0].strip())
    M = int(line[1].strip())

    # Make the board
    board = []
    for j in range(0, N):
        lineB = file.readline().replace("\n","");
        lineB = lineB.split(" ")
        for num in lineB:
            num = int(num)

        board.append(lineB)

    # Test the board!
    ans = checkBoard(N, M, board)
    print( "Case #" + str(i+1) + ": " + ans )
    

file.close()






