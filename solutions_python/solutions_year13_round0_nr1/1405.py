from sys import stdin

input_it = iter(stdin)

T = int(input_it.next())

try:
    for t in range(T):

        # interpret input
        matrix = []
        for i in range(4):
            line = input_it.next()
            row = list(line)[:4]
            matrix.append(row)

        # determine case
        full = not any('.' in row for row in matrix)
        transposed = zip(*matrix)

        xwon = any('.' not in row and 'O' not in row for row in matrix)
        xwon = xwon or any('.' not in row and 'O' not in row for row in transposed)
        xwon = xwon or all(matrix[i][i] not in ('.', 'O') for i in range(4))
        xwon = xwon or all(matrix[i][3-i] not in ('.', 'O') for i in range(4))
        if xwon:
            print 'Case #{}: X won'.format(t+1)
            input_it.next()
            continue

        owon = any('.' not in row and 'X' not in row for row in matrix)
        owon = owon or any('.' not in row and 'X' not in row for row in transposed)
        owon = owon or all(matrix[i][i] not in ('.', 'X') for i in range(4))
        owon = owon or all(matrix[i][3-i] not in ('.', 'X') for i in range(4))
        if owon:
            print 'Case #{}: O won'.format(t+1)
            input_it.next()
            continue

        if full:
            print 'Case #{}: Draw'.format(t+1)
        else:
            print 'Case #{}: Game has not completed'.format(t+1)
        input_it.next()

except StopIteration:
    pass
