from sys import stdin

input_it = iter(stdin)

T = int(input_it.next())

for t in range(T):

    # interpret input
    N, M = (int(c) for c in input_it.next().split())
    matrix = []
    for n in range(N):
        line = input_it.next()
        row = [int(h) for h in line.split()]
        matrix.append(row)

    # determine case
    transposed = zip(*matrix)
    max_per_row = [max(row) for row in matrix]
    max_per_col = [max(row) for row in transposed]
    result = True
    for row in range(N):
        for col in range(M):
            if matrix[row][col] < max_per_row[row] and matrix[row][col] < max_per_col[col]:
                result = False
                break
        if result == False:
            break

    if result == False:
        print 'Case #{}: NO'.format(t+1)
    else:
        print 'Case #{}: YES'.format(t+1)
