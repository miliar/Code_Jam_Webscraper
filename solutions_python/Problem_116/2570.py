def check(c, lines):
    for line in lines:
        if line.count(c) == 3 and line.count('T') == 1:
            return True

        if line.count(c) == 4:
            return True

    return False

    

fin = open('A-large.in', 'rb')
fout = open('a.txt', 'wb')

T = int(fin.readline().strip())
lines = fin.readlines()

for case in range(T):
    rows = [line.strip() for line in lines[5 * case : 5 * case + 4]]
    cols = [''.join(row[i] for row in rows) for i in range(4)]
    diag1 = [''.join(rows[i][i] for i in range(4))]
    diag2 = [''.join(rows[i][3 - i] for i in range(4))]

    linesToCheck = rows + cols + diag1 + diag2

    if check('X', linesToCheck):
        fout.write('Case #' + str(case + 1) + ': X won\n')
    elif check('O', linesToCheck):
        fout.write('Case #' + str(case + 1) + ': O won\n')
    elif sum(row.count('.') for row in rows) > 0:
        fout.write('Case #' + str(case + 1) + ': Game has not completed\n')
    else:
        fout.write('Case #' + str(case + 1) + ': Draw\n')

