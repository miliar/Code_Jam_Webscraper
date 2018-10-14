def checkWinner(table):
    full = True
    for line in table:
        won = True

        if line.count('.') > 0:
            won = False
            full = False

        xCount = line.count('X')
        oCount = line.count('O')

        if xCount > 0 and oCount > 0:
            won = False
        elif xCount > 0:
            who = 'X'
        else:
            who = 'O'

        if won:
            return who + " won"

    if full:
        return "Draw"
    else:
        return "Game has not completed"


f = open('1-small-practice.in.txt', 'r')
fw = open('1-small-out.txt', 'w')

for i in xrange(int(f.readline())):
    table = []
    for j in xrange(4):
        table.append(f.readline())
        if table[j][-1] == '\n':
            table[j] = table[j][:-1]

    diag = ''
    xDiag = ''
    for x in xrange(4):
        col = ''
        for y in xrange(4):
            col += table[y][x]
            if x == y:
                diag += table[x][y]
            if x+y == 3:
                xDiag += table[x][y]
        table.append(col)
    table.append(diag)
    table.append(xDiag)
    
    f.readline()

    fw.write('Case #' + str(i+1) + ': ' + checkWinner(table) + '\n')

fw.close()
f.close()
