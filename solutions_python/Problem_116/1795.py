# Joseph Lee
# Qualification Round
# 4/12/13
# Problem A


def test_case(rows):
    incomplete = False

    # test row-wise winners
    for row in rows:
        if '.' not in row:
            if 'X' not in row:
                return 'O won'
            elif 'O' not in row:
                return 'X won'
        else:
            incomplete = True
    
    # test col-wise winners
    for c in xrange(0, 4):
        col = rows[0][c], rows[1][c], rows[2][c], rows[3][c]
        if '.' not in col:
            if 'X' not in col:
                return 'O won'
            elif 'O' not in col:
                return 'X won'

    # test diag-wise winners
    diag = []
    for i in xrange(0, 4):
        diag.append(rows[i][i])
    if '.' not in diag:
        if 'X' not in diag:
            return 'O won'
        elif 'O' not in diag:
            return 'X won'
    diag = []
    for i in reversed(xrange(0, 4)):
        diag.append(rows[3 - i][i])
    if '.' not in diag:
        if 'X' not in diag:
            return 'O won'
        elif 'O' not in diag:
            return 'X won'

    if incomplete:
        return 'Game has not completed'
    return 'Draw'


def main():
    from sys import argv
    fname = argv[1]
    infile = open(fname, 'r')
    data = infile.readlines()
    infile.close()

    count = 1
    while len(data) > 0:
        case, data = data[0:5], data[5:]
        case.pop(0)
        if len(case) == 4:
            print 'Case #%d: %s' % (count, test_case(case))
            count += 1

if __name__ == '__main__':
    main()
