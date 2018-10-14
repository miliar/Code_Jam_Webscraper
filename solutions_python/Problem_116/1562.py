import sys

tests = int(sys.stdin.readline())
for i in range(1, tests+1):
    output = "Case #" + str(i) + ":"
    result = ""

    emptyFound = False
    resultKnown = False
    columns = [0]*8
    diagonals = [0]*4
    for j in range(4):
        squares = sys.stdin.readline()
        if resultKnown: continue
        rows = [0]*2
        for k in range(4):
            if squares[k] == 'X':
                rows[0] = rows[0]*2+1
                rows[1] = rows[1]*2+1
                columns[k] = columns[k]*2+1
                columns[k+4] = columns[k]*2+1
                if j==k:
                    diagonals[0] = diagonals[0]*2+1
                    diagonals[2] = diagonals[2]*2+1
                elif j==3-k:
                    diagonals[1] = diagonals[1]*2+1
                    diagonals[3] = diagonals[3]*2+1
            elif squares[k] == 'O':
                rows[0] = rows[0]*2-1
                rows[1] = rows[1]*2-1
                columns[k] = columns[k]*2-1
                columns[k+4] = columns[k+4]*2-1
                if j==k:
                    diagonals[0] = diagonals[0]*2-1
                    diagonals[2] = diagonals[2]*2-1
                elif j==3-k:
                    diagonals[1] = diagonals[1]*2-1
                    diagonals[3] = diagonals[3]*2-1
            elif squares[k] == '.':
                emptyFound = True
            elif squares[k] == 'T':
                rows[0] = rows[0]*2+1
                rows[1] = rows[1]*2-1
                columns[k] = columns[k]*2+1
                columns[k+4] = columns[k+4]*2-1
                if j==k:
                    diagonals[0] = diagonals[0]*2+1
                    diagonals[2] = diagonals[2]*2-1
                elif j==3-k:
                    diagonals[1] = diagonals[1]*2+1
                    diagonals[3] = diagonals[3]*2-1
        if 15 in rows:
            result = "X won"
            resultKnown = True
        elif -15 in rows:
            result = "O won"
            resultKnown = True

    if 15 in columns or 15 in diagonals:
        result = "X won"
    elif -15 in columns or -15 in diagonals:
        result = "O won"
    elif emptyFound:
        result = "Game has not completed"
    elif not resultKnown:
        result = "Draw"

    print(output, result)
    line = sys.stdin.readline()