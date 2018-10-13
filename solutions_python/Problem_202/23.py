import sys

T = int(raw_input())
idx = 1

# Marix: 0 - empty, 1 - empty && can't place, 2 - placed
def place_mark(matrix, row, col, stats):
    matrix[row][col] = 2
    stats[row] -= 1

    n = len(matrix)
    for i in xrange(n):
        if matrix[row][i] == 0:
            matrix[row][i] = 1
            stats[row] -= 1
        if matrix[i][col] == 0:
            matrix[i][col] = 1
            stats[i] -= 1

def try_place(matrix, stats):
    n = len(matrix)
    while True:
        # select min index
        min_index = -1
        min_stat = n + 1
        for i in xrange(n):
            if stats[i] > 0 and stats[i] < min_stat:
                min_index = i
                min_stat = stats[i]
        if min_index == -1:
            return

        for col in xrange(n):
            if matrix[min_index][col] == 0:
                place_mark(matrix, min_index, col, stats)
                break
        else:
            assert False # Please no here
        

def solve(n, pre_placed):
    p = 2 * n + 1
    normal_matrix = [[0] * n for x in xrange(n)]
    normal_stats = [n] * n
    dia_matrix = [[1] * p for x in xrange(p)]
    dia_stats = [0] * p
    for x in xrange(n):
        for y in xrange(n):
            dia_matrix[x + y][x - y + n - 1] = 0
            dia_stats[x + y] += 1

    for item in pre_placed:
        token, row, col = item
        if token == 'o' or token == 'x':
            place_mark(normal_matrix, row, col, normal_stats)
        if token == 'o' or token == '+':
            new_row = row + col
            new_col = row - col + n - 1

            place_mark(dia_matrix, new_row, new_col, dia_stats)

    try_place(normal_matrix, normal_stats)
    try_place(dia_matrix, dia_stats)

    checks = set(pre_placed)
    outs = []
    ans = 0
    for x in xrange(n):
        for y in xrange(n):
            token = 0
            if normal_matrix[x][y] == 2:
                token += 1
                ans += 1
            if dia_matrix[x+y][x-y+n-1] == 2:
                token += 2
                ans += 1
                
            if token != 0:
                token = 'x+o'[token - 1]
                if (token, x, y) not in checks:
                    outs.append("%s %s %s" % (token, x + 1, y + 1))

    if outs:
        return "%s %s\n%s" % (ans, len(outs), '\n'.join(outs))
    else:
        return "%s %s" % (ans, 0)
            
while T > 0:
    n, m = map(int, raw_input().split())
    pre_placed = []
    for i in range(m):
        token, x, y = raw_input().split()
        x = int(x) - 1
        y = int(y) - 1
        pre_placed.append((token, x, y))
  
    print "Case #%s: %s" % (idx, solve(n, pre_placed))
    idx += 1
    T -= 1
