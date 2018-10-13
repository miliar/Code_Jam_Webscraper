from sys import stdin


def compute(grid, R):
    g = grid
    for row in g:
        now = '?'
        for i, char in enumerate(row):
            if char != '?':
                now = char
                for x in range(1, i+1):
                    if row[i-x] == '?':
                        row[i-x] = now
                    else:
                        break
            else:
                row[i] = now
    for i, row in enumerate(g):
        if row != list('?' * len(row)):
            good_row = row
            break

    for i, row in enumerate(g):
        if row == list('?' * len(row)):
            g[i] = good_row
        else:
            good_row = row

    return g


T = int(input())

for case in range(1, T+1):
    R, C = list(map(int, stdin.readline().split(' ')))
    grid = [list(stdin.readline().strip()) for x in range(0, R)]
    h = compute(grid, R)
    print("Case #{}:".format(case))
    for row in h:
        print("".join(row))
