t = int(input())

def do_case(debug=False):
    n, m = map(int, input().split())
    data = [[[False, False] for j in range(n)] for i in range(n)]
    changed = [[False] * n for i in range(n)]
    for i in range(m):
        char, r, c = input().split()
        r = int(r)
        c = int(c)
        data_point = data[r - 1][c - 1]
        if char in ("x", "o"):
            data_point[0] = True
        if char in ("+", "o"):
            data_point[1] = True

    def debug_print():
        if not debug:
            return
        for row in data:
            for data_point in row:
                c = "."
                if data_point == [True, False]:
                    c = "x"
                elif data_point == [False, True]:
                    c = "+"
                elif data_point == [True, True]:
                    c = "o"
                print(c, end="")
            print()
        print()

    debug_print()

    x = 0
    y = 0
    while x < n and y < n:
        row_ok = True
        for x1 in range(n):
            if data[y][x1][0]:
                row_ok = False
                break
        col_ok = True
        for y1 in range(n):
            if data[y1][x][0]:
                col_ok = False
                break
        if col_ok and row_ok:
            data[y][x][0] = True
            changed[y][x] = True
            y += 1
            x += 1
        elif row_ok and x < n:
            x += 1
        elif col_ok and y < n:
            y += 1
        else:
            x += 1
            y += 1

    #debug_print()

    def diag_check(x, y, dx, dy):
        while x >= 0 and y >= 0 and x < n and y < n:
            if data[y][x][1]:
                return False
            x += dx
            y += dy
        return True


    for k in range(n):
        for l in range(k + 1):
            x = l
            y = k - l
            if diag_check(x, y, 1, 1) and \
                diag_check(x, y, 1, -1) and \
                diag_check(x, y, -1, -1) and \
                diag_check(x, y, -1, 1):
                data[y][x][1] = True
                changed[y][x] = True
            x = n - 1 - x
            y = n - 1 - y
            if diag_check(x, y, 1, 1) and \
                diag_check(x, y, 1, -1) and \
                diag_check(x, y, -1, -1) and \
                diag_check(x, y, -1, 1):
                data[y][x][1] = True
                changed[y][x] = True

    debug_print()

    points = sum(sum(map(sum, row)) for row in data)

    list_of_changes = []
    for y, row in enumerate(data):
        for x, data_point in enumerate(row):
            if changed[y][x]:
                c = " "
                if data_point == [True, False]:
                    c = "x"
                elif data_point == [False, True]:
                    c = "+"
                elif data_point == [True, True]:
                    c = "o"
                list_of_changes.append("{} {} {}".format(c, y + 1, x + 1))
    output = "\n".join(["{} {}".format(points, len(list_of_changes))] + list_of_changes)

    return output

for task in range(t):
    output = do_case(False)
    print("Case #{}: {}".format(task + 1, output))
