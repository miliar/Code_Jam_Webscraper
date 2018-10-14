def solve(casenum):
    rows, cols = map(int, raw_input().strip().split())
    matrix = [list(raw_input()) for row in xrange(rows)]

    #Go right
    for row in xrange(rows):
        current = '?'
        for col in xrange(cols):
            if matrix[row][col] == '?':
                matrix[row][col] = current
            elif matrix[row][col] != current:
                current = matrix[row][col]
    
    #Go left
    for row in xrange(rows):
        current = '?'
        for col in xrange(cols - 1, -1, -1):
            if matrix[row][col] == '?':
                matrix[row][col] = current
            elif matrix[row][col] != current:
                current = matrix[row][col]

    #Go down
    for col in xrange(cols):
        current = '?'
        for row in xrange(rows):
            if matrix[row][col] == '?':
                matrix[row][col] = current
            elif matrix[row][col] != current:
                current = matrix[row][col]
    
    #Go up
    for col in xrange(cols):
        current = '?'
        for row in xrange(rows - 1, -1, -1):
            if matrix[row][col] == '?':
                matrix[row][col] = current
            elif matrix[row][col] != current:
                current = matrix[row][col]
    
    print 'Case #%d:' % casenum
    print '\n'.join(''.join(row) for row in matrix)

for i in xrange(1, input() + 1):
    solve(i)
