def solve(rows):
    newrows = [[c for c in row] for row in rows]
    for i, row in enumerate(newrows):
        for j, tile in enumerate(row):
            if tile == '#':
                if j + 1 >= len(row) or row[j+1] == '.' or \
                   i + 1 >= len(newrows) or newrows[i+1][j] == '.' or \
                   newrows[i+1][j+1] == '.':
                       return "Impossible"
                newrows[i][j] = '/'
                newrows[i][j+1] = '\\'
                newrows[i+1][j] = '\\'
                newrows[i+1][j+1] = '/'
    return '\n'.join([''.join(row) for row in newrows])

t = int(input())
for case in range(t):
    line = input().split(' ')
    r, _ = map(int, line)
    rows = []
    for _ in range(r):
        rows.append(input())
    print("Case #%d:" % (case + 1))
    print(solve(rows))
