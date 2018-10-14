def get_rep(x, y, r, c):
    if x < c - 2:
        i = x + 1
        while i < c and arr[i][y] == '?':
            i += 1
        if i < c:
            for j in range(x, i):
                arr[j][y] = arr[i][y]
            return
    if y < r - 2:
        i = y + 1
        while  i < r and arr[x][i] == '?':
            i += 1
        if i < r:
            for j in range(y, i):
                arr[x][j] = arr[x][i]
            return
    if x > 1:
        i = x - 1
        while i > 0 and arr[i][y] == '?':
            i -= 1
        if i > 0:
            for j in range(i+1, x+1):
                arr[j][y] = arr[i][y]
            return
    if y > 1:
        i = y - 1
        while i > 0 and arr[x][i] == '?':
            i -= 1
        if i > 0:
            for j in range(i+1, y+1):
                arr[x][j] = arr[x][i]
            return
    return

def fill_row(x,y):
    i = x - 1
    while i >= 0 and arr[y][i] == '?':
        arr[y][i] = arr[y][x]
        i -= 1
    i = x + 1
    while i < C and arr[y][i] == '?':
        arr[y][i] = arr[y][x]
        i += 1
    return i

def fill_col(x,y):
    j = y - 1
    changed = False
    while j >= 0 and arr[j][x] == '?':
        changed = True
        arr[j][x] = arr[y][x]
        j -= 1
    j = y + 1
    while j < R and arr[j][x] == '?':
        changed = True
        arr[j][x] = arr[y][x]
        j += 1
    return j if changed else -1

with open('input.in', 'r') as f:
    with open('output.out', 'w') as out:
        t = int(f.readline())

        for i in range(1, t+1):
            s = f.readline().strip()
            while not s:
                s = f.readline().strip()
            R, C = [int(x) for x in s.split()]
            arr = R * [0]
            for r in range(R):
                s = f.readline().strip()
                arr[r] = list(s)
            for r in range(R):
                for c in range(C):
                    if arr[r][c] != '?':
                        last_index = fill_row(c, r)
                        while last_index < C - 1 and last_index != -1:
                            last_index = fill_row(last_index, r)
            for c in range(C):
                for r in range(R):
                    if arr[r][c] != '?':
                        last_index = fill_col(c, r)
                        while last_index < R - 1 and last_index != -1:
                            last_index = fill_col(c, last_index)




            out.write("Case #" + str(i) + ":\n")
            for r in range(R):
                for c in range(C):
                    out.write(arr[r][c])
                out.write("\n")
