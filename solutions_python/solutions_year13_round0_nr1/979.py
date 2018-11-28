import sys

f = open(sys.argv[1])
T = int(f.readline())

for t in range(T):
    field = []
    # add rows
    for i in range(4):
        line = f.readline().strip()
        row = []
        for letter in line:
            if letter == 'O':
                row.append(-1)
            elif letter == 'T':
                row.append(0)
            elif letter == 'X':
                row.append(1)
            else:
                row.append(None)
        field.append(row)
    # add columns
    for i in range(4):
        column = []
        for j in range(4):
            column.append(field[j][i])
        field.append(column)
    # add diagonals
    diagonals = [[], []]
    for i in range(4):
        diagonals[0].append(field[i][i])
        diagonals[1].append(field[3-i][i])
    field.extend(diagonals)

    status = 'Draw'

    # solve game
    for row in field:
        if None in row:
            status = 'Game has not completed'
        elif sum(row) <= -3:
            status = 'O won'
            break
        elif sum(row) >= 3:
            status = 'X won'
            break

    print 'Case #%s: %s' % (t+1, status)
    # skip empty line
    f.readline()


