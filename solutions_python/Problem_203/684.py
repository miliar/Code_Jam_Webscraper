def fill(cake, fx, fy, tx, ty, color):
    for i in range(fx, tx):
        for j in range(fy, ty):
            cake[i][j] = color


def rescue_from_row(cake, fx, fy, tx, ty):
    for i in range(fx, tx):
        for j in range(fy, ty):
            cake[i][j] = cake[i][fy - 1]


def rescue_from_col(cake, fx, fy, tx, ty):
    for i in range(fx, tx):
        for j in range(fy, ty):
            cake[i][j] = cake[fx - 1][j]


def divide(cake, fx, fy, tx, ty):
    small_cake = [[] for i in range(fx, tx)]
    for i in range(fx, tx):
        for j in range(fy, ty):
            small_cake[i - fx].append(cake[i][j])

    for i in range(fx, tx):
        for j in range(fy, ty):
            if cake[i][j] != '?':
                current_color = cake[i][j]
                fill(cake, fx, fy, i + 1, j + 1, current_color)
                if divide(cake, fx, j + 1, i + 1, ty):  # 2/4 is blank!

                    fill(cake, fx, j + 1, i + 1, ty, current_color)
                    if divide(cake, i + 1, fy, tx, ty):
                        fill(cake, i + 1, fy, tx, ty, current_color)
                else:
                    if divide(cake, i + 1, fy, tx, j + 1):  # 3/4 is blank!
                        fill(cake, i + 1, fy, tx, j + 1, current_color)
                        if divide(cake, i + 1, j + 1, tx, ty):
                            rescue_from_col(cake, i + 1, j + 1, tx, ty)
                            # fill(cake, fx, j + 1, tx, ty, current_color)
                    else:
                        if divide(cake, i + 1, j + 1, tx, ty):  # 4/4 is only blank lol
                            rescue_from_row(cake, i + 1, j + 1, tx, ty)
                return False
    return True


def solve(r, c, cake):
    divide(cake, 0, 0, r, c)

# f = open('A-small-attempt0.in')
# for t in range(1, int(f.readline()) + 1):
#     r, c = map(int, f.readline().strip().split())
#     cake = [list(f.readline().strip()) for x in range(r)]
for t in range(1, int(raw_input()) + 1):
    r, c = map(int, raw_input().strip().split())
    cake = [list(raw_input().strip()) for x in range(r)]
    solve(r, c, cake)
    print 'Case #%d:' % t
    for sol_line in cake:
        print "".join(sol_line)
