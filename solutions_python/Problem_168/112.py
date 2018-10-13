from sys import stdin

def helper(x):
    if x == '^': return 1
    if x == 'v': return 2
    if x == '<': return 4
    return 8

T = int(stdin.readline())

for no in range(T):
    R, C = map(int, stdin.readline().split())
    grid = []
    for i in range(R):
        grid.append(stdin.readline().strip())

    cons = [[0] * C for i in range(R)]

    ans = 0

    for j in range(C):
        for i in range(R):
            if grid[i][j] != '.':
                cons[i][j] |= 1
                break
    for j in range(C):
        for i in range(R-1, -1, -1):
            if grid[i][j] != '.':
                cons[i][j] |= 2
                break
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '.':
                cons[i][j] |= 4
                break
    for i in range(R):
        for j in range(C-1, -1, -1):
            if grid[i][j] != '.':
                cons[i][j] |= 8
                break

    impossible = False

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.': continue
            if cons[i][j] == 15: impossible = True
            if cons[i][j] & helper(grid[i][j]): ans += 1

    print 'Case #{}:'.format(no+1),
    if impossible:
        print 'IMPOSSIBLE'
    else:
        print ans
