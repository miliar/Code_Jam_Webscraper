def RowCheck(Map):
    for i in Map:
        if (i[0] == 'X') or (i[0] == 'T'):
            if (i[1] == 'X') or (i[1] == 'T'):
                if (i[2] == 'X') or (i[2] == 'T'):
                    if (i[3] == 'X') or (i[3] == 'T'):
                        return 'X'
        elif (i[0] == 'O') or (i[0] == 'T'):
            if (i[1] == 'O') or (i[1] == 'T'):
                if (i[2] == 'O') or (i[2] == 'T'):
                    if (i[3] == 'O') or (i[3] == 'T'):
                        return 'O'
    return 'Draw'

def ColumnCheck(Map):
    x = 0
    while(x<4):
        if (Map[0][x] == 'X') or (Map[0][x] == 'T'):
            if (Map[1][x] == 'X') or (Map[1][x] == 'T'):
                if (Map[2][x] == 'X') or (Map[2][x] == 'T'):
                    if (Map[3][x] == 'X') or (Map[3][x] == 'T'):
                        return 'X'
        if (Map[0][x] == 'O') or (Map[0][x] == 'T'):
            if (Map[1][x] == 'O') or (Map[1][x] == 'T'):
                if (Map[2][x] == 'O') or (Map[2][x] == 'T'):
                    if (Map[3][x] == 'O') or (Map[3][x] == 'T'):
                        return 'O'
        x = x+1
    return 'Draw'
def diagonalCheck(Map):
     if (Map[0][0] == 'X') or (Map[0][0] == 'T'):
        if (Map[1][1] == 'X') or (Map[1][1] == 'T'):
            if (Map[2][2] == 'X') or (Map[2][2] == 'T'):
                if (Map[3][3] == 'X') or (Map[3][3] == 'T'):
                        return 'X'
     if (Map[0][3] == 'X') or (Map[0][3] == 'T'):
        if (Map[1][2] == 'X') or (Map[1][2] == 'T'):
            if (Map[2][1] == 'X') or (Map[2][1] == 'T'):
                if (Map[3][0] == 'X') or (Map[3][0] == 'T'):
                        return 'X'
     if (Map[0][0] == 'O') or (Map[0][0] == 'T'):
        if (Map[1][1] == 'O') or (Map[1][1] == 'T'):
            if (Map[2][2] == 'O') or (Map[2][2] == 'T'):
                if (Map[3][3] == 'O') or (Map[3][3] == 'T'):
                        return 'O'
     if (Map[0][3] == 'O') or (Map[0][3] == 'T'):
        if (Map[1][2] == 'O') or (Map[1][2] == 'T'):
            if (Map[2][1] == 'O') or (Map[2][1] == 'T'):
                if (Map[3][0] == 'O') or (Map[3][0] == 'T'):
                        return 'O'
     return 'Draw'
def GameFinCheck(Map):
    for line in Map:
        for sqr in line:
            if (sqr == '.'):
                return 'Not Completed'
            else:
                pass
    return 'Completed'

Infile = open('A-small-attempt0.in','r')
Outfile = open('output.txt','w')
caseNo = int(Infile.readline())
casecount = 0
while(casecount < caseNo):
    board = []
    i = 0
    while (i<4):
        line = Infile.readline()
        board.append(line.strip('\n'))
        i = i+1
    print board
    row = RowCheck(board)
    if (row == 'Draw'):
        column = ColumnCheck(board)
        if (column == 'Draw'):
            diagonal = diagonalCheck(board)
            if (diagonal == 'Draw'):
                if (GameFinCheck(board) == 'Completed'):
                    result = 'Draw'
                else:
                    result = 'Game has not completed'
            else:
                result = diagonal + ' won'
        else:
            result = column+' won'
    else:
        result = row+' won'
    num = str(casecount+1)
    output = 'Case #%s: %s \n'%(num,result)
    Outfile.write(output)
    blank = Infile.readline()
    casecount = casecount+1
Infile.close()
Outfile.close()





    
    
