import sys

def checkCol(row):
    for i in range(4):
        if (( row[0][i] == 'X' or row[0][i] == 'T' ) and
            ( row[1][i] == 'X' or row[1][i] == 'T' ) and
            ( row[2][i] == 'X' or row[2][i] == 'T' ) and
            ( row[3][i] == 'X' or row[3][i] == 'T' )):
                    return 'X won'
                
        elif ( ( row[0][i] == 'O' or row[0][i] == 'T' ) and
                ( row[1][i] == 'O' or row[1][i] == 'T' ) and
                ( row[2][i] == 'O' or row[2][i] == 'T' ) and
                ( row[3][i] == 'O' or row[3][i] == 'T' )):
                     return 'O won'


def checkRow(row):
    for each_row in row:
        if each_row == 'XXXX' or \
            each_row == 'TXXX' or \
            each_row == 'XTXX' or \
            each_row == 'XXTX' or \
            each_row == 'XXXT':
                return 'X won'

        elif each_row == 'OOOO' or \
            each_row == 'TOOO' or \
            each_row == 'OTOO' or \
            each_row == 'OOTO' or \
            each_row == 'OOOT':
                return 'O won'
                

def checkDiagonal(row):
    if (( row[0][0] == 'X' or row[0][0] == 'T') and
        ( row[1][1] == 'X' or row[1][1] == 'T') and
        ( row[2][2] == 'X' or row[2][2] == 'T') and
        ( row[3][3] == 'X' or row[3][3] == 'T')):
            return 'X won'

    if ((row[0][3] == 'X' or row[0][3] == 'T') and
        (row[1][2] == 'X' or row[1][2] == 'T') and
        (row[2][1] == 'X' or row[2][1] == 'T') and
        (row[3][0] == 'X' or row[3][0] == 'T')):
            return 'X won'

    if ((row[0][0] == 'O' or row[0][0] == 'T') and
        (row[1][1] == 'O' or row[1][1] == 'T') and
        (row[2][2] == 'O' or row[2][2] == 'T') and
        (row[3][3] == 'O' or row[3][3] == 'T')):
            return 'O won'

    if ((row[0][3] == 'O' or row[0][3] == 'T') and
        (row[1][2] == 'O' or row[1][2] == 'T') and
        (row[2][1] == 'O' or row[2][1] == 'T') and
        (row[3][0] == 'O' or row[3][0] == 'T')):
            return 'O won'


def checkIncomplete(row):
    for each_row in row:
        if '.' in each_row:
            return True

    return False


def algo(filename):
    try:
        infile = open(filename+'.in', 'r')
        outfile = open(filename+'.out', 'w')
    except IOError:
        return

    T = int(infile.readline())
    
    for each_t in range(T):
        row = []
        for each_line in range(4):
            row.append(infile.readline().strip())

        status = ''
        incomplete = checkIncomplete(row)
        status = checkRow(row)
        if not 'won' in str(status):
            status = checkCol(row)
            if not 'won' in str(status):
                status = checkDiagonal(row)
                if not 'won' in str(status):
                    if incomplete == True:
                        status = 'Game has not completed'
                    else:
                        status = 'Draw'

        outfile.write("Case #{0}: {1}\n".format(each_t+1, status))

        infile.readline()

    infile.close()
    outfile.close()



if __name__ == '__main__':
    if len(sys.argv) > 1:
        algo(sys.argv[1])
    else:
        print "No input"
