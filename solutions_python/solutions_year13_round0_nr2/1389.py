import sys

MAX_HEIGHT = 100

tests = int(sys.stdin.readline())
for i in range(1, tests+1):
    output = "Case #" + str(i) + ":"
    result = "YES"

    lawn = []
    lawnRows = {MAX_HEIGHT+1: set()}
    lawnColumns = {MAX_HEIGHT+1: set()}
    line = sys.stdin.readline().split()
    n = int(line[0])
    m = int(line[1])

    for j in range(n):
        line = sys.stdin.readline()
        squares = line.split()
        lawn.append([int(square) for square in squares])
        for k in range(m):
            h = int(squares[k])
            if not lawnRows.get(h):
                lawnRows[h] = set()
            lawnRows[h].add(j)

            if not lawnColumns.get(h):
                lawnColumns[h] = set()
            lawnColumns[h].add(k)

    for h in reversed(range(2, MAX_HEIGHT+1)):
        if not lawnRows.get(h):
            lawnRows[h] = set()
        lawnRows[h] = lawnRows[h].union(lawnRows[h+1])

        if not lawnColumns.get(h):
            lawnColumns[h] = set()
        lawnColumns[h] = lawnColumns[h].union(lawnColumns[h+1])

    for j in range(n):
        if result == "NO": break
        for k in range(m):
            h = lawn[j][k]
            if j in lawnRows.get(h+1) and k in lawnColumns.get(h+1):
                result = "NO"
                break

    print(output, result)