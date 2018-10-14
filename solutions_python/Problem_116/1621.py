import sys


def winner(g, j):
    return ((g[j][0] == g[j][1] == g[j][2] == g[j][3]) or
           (g[0][j] == g[1][j] == g[2][j] == g[3][j]) or
           ((j == 0) and (g[0][0] == g[1][1] == g[2][2] == g[3][3])) or
           ((j == 3) and (g[3][0] == g[2][1] == g[1][2] == g[0][3])))


lines = [line[:-1] for line in sys.stdin.readlines()]
grid = [(i, j) for i in range(4) for j in range(4)]

l = 1
for i in range(int(lines[0])):
    g1 = lines[l:l + 4]
    g2 = None

    found = False
    incomplete = False
    for j, k in grid:
        if g1[j][k] == 'T':
            g2 = lines[l:l + 4]
            g1[j] = g1[j][:k] + 'X' + g1[j][k + 1:]
            g2[j] = g2[j][:k] + 'O' + g2[j][k + 1:]
            found = True
        if g1[j][k] == '.':
            incomplete = True
            if found:
                break

    x_won = y_won = False
    grids = [g for g in [g1, g2] if g is not None]
    for g in grids:
        for j in range(4):
            if not winner(g, j):
                continue
            if (g[j][j] == 'X'
                or (j == 0 and g[0][0] == 'X')
                or (j == 3 and g[3][0] == 'X')):
                x_won = True
            elif (g[j][j] == 'O'
                  or (j == 0 and g[0][0] == 'O')
                  or (j == 3 and g[3][0] == 'O')):
                y_won = True
            break

    if x_won and y_won or not (x_won or y_won or incomplete):
        print('Case #{}: Draw'.format(i + 1))
    elif x_won:
        print('Case #{}: X won'.format(i + 1))
    elif y_won:
        print('Case #{}: O won'.format(i + 1))
    elif not x_won and not y_won:
        print('Case #{}: Game has not completed'.format(i + 1))

    l += 5

