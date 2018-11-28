# coding=utf-8 *** gatopeich for Google Code Jam 2014

# Problem C. Minesweeper Master

filename = 'C-large'

next_line = open(filename + '.in').readline
out = open(filename + '.out', 'w')


def write(*line):
    print(*line, file=out)
    print(*line)


T = int(next_line())
print(T, "cases")

for case in range(1, T + 1):
    write('Case #%d:' % case)
    R, C, M = map(int, next_line().split())
    print(R, C, M, end=' - ')

    # Ensure C <= R
    transposed = R < C
    if transposed:
        R, C = C, R

    field = [['*'] * C for row in range(R)]

    need_free = R * C - M
    if need_free<1:
        write('Impossible')
        continue

    if C == 1:
        for row in range(need_free):
            field[row][0] = '.'
    elif need_free > 1:  # Otherwise just the 'c' spot at 0,0

        empty_cols = C
        if need_free < 2 * empty_cols:
            empty_cols = need_free//2
            if empty_cols < 2:
                write('Impossible')
                continue

        empty_rows = need_free//empty_cols
        for row in range(empty_rows):
            field[row] = list('.'*empty_cols + '*'*(C-empty_cols))
            need_free -= empty_cols

        if need_free == 0:
            pass
        elif need_free > 1:
            field[empty_rows] = list('.'*need_free + '*'*(C-need_free))
        elif empty_cols<3 or empty_rows>=R:
            write('Impossible')
            continue
        elif empty_rows>2:
            field[empty_rows][0] = '.'
            field[empty_rows][1] = '.'
            field[empty_rows-1][empty_cols-1] = '*'
        elif empty_rows==2 and empty_cols>3:
            field[0][empty_cols-1] = '*'
            field[1][empty_cols-1] = '*'
            field[2][0] = '.'
            field[2][1] = '.'
            field[2][2] = '.'
        else:
            write('Impossible')
            continue

    print()
    field[0][0] = 'c'
    if transposed: field = zip(*field)
    field = tuple(map(''.join,field))
    for row in field: write(''.join(row))

    assert ''.join(field).count('*') == M
    assert ''.join(field).count('.') == R*C - M - 1
    assert ''.join(field).count('c') == 1

out.close()

