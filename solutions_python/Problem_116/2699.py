file = open("A-small-attempt0.in", 'r') #Open the local file input
case = 0
checkNum = 0
lines = []
cell = ['.', '.', '.', '.',
        '.', '.', '.', '.',
        '.', '.', '.', '.',
        '.', '.', '.', '.']

def validate(theCase):
    theCase = theCase+1
    winX = False
    winO = False
    #Check horizontal
    if (cell[0] == 'X' or cell[0] == 'T') and (cell[1] == 'X' or cell[1] == 'T') and (cell[2] == 'X' or cell[2] == 'T') and (cell[3] == 'X' or cell[3] == 'T'):
        winX = True
    if (cell[0] == 'O' or cell[0] == 'T') and (cell[1] == 'O' or cell[1] == 'T') and (cell[2] == 'O' or cell[2] == 'T') and (cell[3] == 'O' or cell[3] == 'T'):
        winO = True

    #Check Vertical - 1st COLUMN
    if (cell[0] == 'X' or cell[0] == 'T') and (cell[4] == 'X' or cell[4] == 'T') and (cell[8] == 'X' or cell[8] == 'T') and (cell[12] == 'X' or cell[12] == 'T'):
        winX = True
    if (cell[0] == 'O' or cell[0] == 'T') and (cell[4] == 'O' or cell[4] == 'T') and (cell[8] == 'O' or cell[8] == 'T') and (cell[12] == 'O' or cell[12] == 'T'):
        winO = True

    #Check Vertical - 2nd COLUMN
    if (cell[1] == 'X' or cell[1] == 'T') and (cell[5] == 'X' or cell[5] == 'T') and (cell[9] == 'X' or cell[9] == 'T') and (cell[13] == 'X' or cell[13] == 'T'):
        winX = True
    if (cell[1] == 'O' or cell[1] == 'T') and (cell[5] == 'O' or cell[5] == 'T') and (cell[9] == 'O' or cell[9] == 'T') and (cell[13] == 'O' or cell[13] == 'T'):
        winO = True

    #Check Vertical - 3rd COLUMN
    if (cell[2] == 'X' or cell[2] == 'T') and (cell[6] == 'X' or cell[6] == 'T') and (cell[10] == 'X' or cell[10] == 'T') and (cell[14] == 'X' or cell[14] == 'T'):
        winX = True
    if (cell[2] == 'O' or cell[2] == 'T') and (cell[6] == 'O' or cell[6] == 'T') and (cell[10] == 'O' or cell[10] == 'T') and (cell[14] == 'O' or cell[14] == 'T'):
        winO = True

    #Check Vertical - 4th COLUMN
    if (cell[3] == 'X' or cell[3] == 'T') and (cell[7] == 'X' or cell[7] == 'T') and (cell[11] == 'X' or cell[11] == 'T') and (cell[15] == 'X' or cell[15] == 'T'):
        winX = True
    if (cell[3] == 'O' or cell[3] == 'T') and (cell[7] == 'O' or cell[7] == 'T') and (cell[11] == 'O' or cell[11] == 'T') and (cell[15] == 'O' or cell[15] == 'T'):
        winO = True

    #Check Diagonal - Left to Right
    if (cell[0] == 'X' or cell[0] == 'T') and (cell[5] == 'X' or cell[5] == 'T') and (cell[10] == 'X' or cell[10] == 'T') and (cell[15] == 'X' or cell[15] == 'T'):
        winX = True
    if (cell[0] == 'O' or cell[0] == 'T') and (cell[5] == 'O' or cell[5] == 'T') and (cell[10] == 'O' or cell[10] == 'T') and (cell[15] == 'O' or cell[15] == 'T'):
        winO = True

    #Check Diagonal - Right to Left
    if (cell[3] == 'X' or cell[3] == 'T') and (cell[6] == 'X' or cell[6] == 'T') and (cell[9] == 'X' or cell[9] == 'T') and (cell[12] == 'X' or cell[12] == 'T'):
        winX = True
    if (cell[3] == 'O' or cell[3] == 'T') and (cell[6] == 'O' or cell[6] == 'T') and (cell[9] == 'O' or cell[9] == 'T') and (cell[12] == 'O' or cell[12] == 'T'):
        winO = True

    if winX == True and winO == True:
        lines.append('Case #%s: Draw' % theCase)

    elif winX == True:
        lines.append('Case #%s: X won' % theCase)

    elif winO == True:
        lines.append('Case #%s: O won' % theCase)

    elif winO == False and winX == False:
        line = ''
        try:
            cell.index('.')
            line = 'Case #%s: Game has not completed' % theCase
        except:
            line = 'Case #%s: Draw' % theCase

        lines.append(line)

case = file.readline()
checking = 0
for cases in range(int(case)):
    for x in range(4):
        for y in file.readline().strip():
            cell[checking] = y
            checking += 1
    file.readline()
    validate(int(checkNum))
    checkNum += 1
    checking = 0
    cell = ['.', '.', '.', '.',
            '.', '.', '.', '.',
            '.', '.', '.', '.',
            '.', '.', '.', '.']

lines = '\n'.join(lines)
print lines

output = open('output.txt', 'w')
output.write(lines)
output.close()