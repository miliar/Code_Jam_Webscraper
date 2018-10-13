def displayCake(cake):
    for i in range(len(cake)):
        row = ''
        for j in range(len(cake[0])):
            row += cake[i][j]
        print row

t = int(raw_input())
for i in xrange(1, t + 1):
    rows, cols = [int(s) for s in raw_input().split(" ")]
    cake = []
    for r in range(rows):
        cake.append(list(raw_input()))

    current = ''
    currentRow = -1
    currentCol = -1
    for row in range(rows):
        for col in range(cols):
            if cake[row][col] != '?':
                letter = cake[row][col]
                for j in range(rows):
                    if cake[j][col] != '?' and cake[j][col] != letter:
                        letter = cake[j][col]
                    cake[j][col] = letter

    for row in range(rows):
        for col in range(cols):
            if cake[row][col] != '?':
                letter = cake[row][col]
                for k in range(cols):
                    if cake[row][k] != '?' and cake[row][k] != letter:
                        letter = cake[row][k]
                    cake[row][k] = letter
    print 'Case #' + str(i) + ":"
    displayCake(cake)
