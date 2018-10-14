outfile = open('output.txt', 'w')

cases = int(input())

def in_bounds(row, col, rows, cols):
    return (row >= 0 and col >= 0) and (col < cols and row < rows)

for case in range(cases):
    inp = input().split()
    rows, cols = int(inp[0]), int(inp[1])

    board = [list(input()) for row in range(rows)]

    for row in range(len(board)):
        for col in range(len(board[row])):
            if not board[row][col] == '?':
                counter = 1
                while in_bounds(row+counter, col, rows, cols) and \
                      board[row+counter][col] == '?':
                    board[row+counter][col] = board[row][col]
                    counter += 1

                counter = 1
                while in_bounds(row-counter, col, rows, cols) and \
                      board[row-counter][col] == '?':
                    board[row-counter][col] = board[row][col]
                    counter += 1

    for line in board:
        if '?' in line:
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if not board[row][col] == '?':
                        counter = 1
                        while in_bounds(row, col+counter, rows, cols) and \
                              board[row][col+counter] == '?':
                            board[row][col+counter] = board[row][col]
                            counter += 1

                        counter = 1
                        while in_bounds(row, col-counter, rows, cols) and \
                              board[row][col-counter] == '?':
                            board[row][col-counter] = board[row][col]
                            counter += 1
            break

    outfile.write('Case #' + str(case+1) + ':\n')
    for row in range(len(board)):
        for col in range(len(board[row])):
            outfile.write(board[row][col])
        outfile.write('\n')

outfile.close()
