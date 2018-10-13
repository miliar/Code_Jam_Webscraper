INPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\B-large.in'
OUTPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\B-large.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(board, n, m):
    shadowBoard = []
    for x in range(n):
        shadowBoard.append([1] * m)
    for x in range(n):
        lineMax = max([h for h in board[x] if h != 0])
        for y in range(m):
            if lineMax == board[x][y]:
                shadowBoard[x][y] = 0
    for y in range(m):
        lineMax = 0
        for x in range(n):
            if board[x][y] > lineMax:
                lineMax = board[x][y]
        for x in range(n):
            if lineMax == board[x][y]:
                shadowBoard[x][y] = 0
    total = 0
    for x in range(n):
        total += sum(shadowBoard[x])
    if 0 != total:
        return 'NO'
    return 'YES'

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    l = inputFile.readline().split()
    n = int(l[0])
    m = int(l[1])
    board = []
    for l in range(n):
        r = [int(x) for x in inputFile.readline().split()]
        board.append(r)
    result = solveQuestion(board, n, m)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
