INPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\A-small-attempt0.in'
OUTPUT_FILE = r'C:\Users\assaf\Google Drive\Fun\GoogleCodeJam2013\A-small-attempt0.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def WhoWins(x):
    who = None
    for c in x:
        if 'T' == c:
            continue
        if '.' == c:
            return '.'
        if None == who:
            who = c
        elif c != who:
            who = '-'
    return who

def solveQuestion(board):
    isDraw = True
    for x in range(4):
        who = WhoWins(board[x])
        if '.' == who:
            isDraw = False
        elif '-' != who:
            return '%s won' % who
    for y in range(4):
        who = WhoWins([board[0][y], board[1][y], board[2][y], board[3][y]])
        if '.' == who:
            isDraw = False
        elif '-' != who:
            return '%s won' % who
    who = WhoWins([board[0][0], board[1][1], board[2][2], board[3][3]])
    if '-' != who and '.' != who:
        return '%s won' % who
    if isDraw:
        return 'Draw'
    who = WhoWins([board[0][3], board[1][2], board[2][1], board[3][0]])
    if '-' != who and '.' != who:
        return '%s won' % who
    if isDraw:
        return 'Draw'
    return 'Game has not completed'

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    x = []
    while len(x) != 4:
        line = inputFile.readline()
        line = line.replace('\r', '').replace('\n', '').replace(' ', '')
        if len(line) < 4:
            continue
        row = [line[0],line[1],line[2],line[3]]
        x.append(row)
    result = solveQuestion(x)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
