import numpy as np
inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "
    n, m = [int(x) for x in inf.readline().split()]
    bishops = []
    rooks = []
    rook_cols = [False] * n
    rook_rows = [False] * n
    for i in range(m):
        line = inf.readline().split()
        if line[0] == 'o' or line[0] == '+':
            bishops.append((int(line[1]), int(line[2])))
        if line[0] == 'o' or line[0] == 'x':
            rooks.append((int(line[1]), int(line[2])))
            rook_rows[int(line[1]) - 1] = True
            rook_cols[int(line[2]) - 1] = True

    def check_bishop(r, c):
        for b in bishops:
            if r + c == b[0] + b[1]:
                return False
            if r - c == b[0] - b[1]:
                return False
        return True

    new_bishops = []
    new_rooks = []

    for i in range(n):
        if check_bishop(1, i + 1):
            bishops.append((1, i + 1))
            new_bishops.append((1, i + 1))
        if check_bishop(n, i + 1):
            bishops.append((n, i + 1))
            new_bishops.append((n, i + 1))

    col = 0
    for i in range(n):
        if not rook_rows[i]:
            while rook_cols[col]:
                col += 1
            rook_cols[col] = True
            rook_rows[i] = True
            new_rooks.append((i + 1, col + 1))
    newm = 0
    models = ""
    for i in new_rooks:
        newm += 1
        if i in bishops:
            models += 'o ' + str(i[0]) + ' ' + str(i[1]) + '\n'
        else:
            models += 'x ' + str(i[0]) + ' ' + str(i[1]) + '\n'

    for i in new_bishops:
        if not i in new_rooks:
            newm += 1
            if i in rooks:
                models += 'o ' + str(i[0]) + ' ' + str(i[1]) + '\n'
            else:
                models += '+ ' + str(i[0]) + ' ' + str(i[1]) + '\n'

    rstr += str(len(bishops) + n) + ' ' + str(newm) + '\n'
    rstr += models
    print(rstr)
    outf.write(rstr)
