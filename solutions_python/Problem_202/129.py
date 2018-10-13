def getv(n, a, row, col):
    return a[row * n + col]

def setv(n, a, row, col, v):
    a[row * n + col] = v

def setv_safe(n, a, row, col, v):
    if row < 0 or col < 0: return
    if row >= n or col >= n: return
    setv(n, a, row, col, v)

def set_bishop_disallowed_in_row(n, a, row, col, row_to_set):
    diff = abs(row - row_to_set)
    setv_safe(n, a, row_to_set, col + diff, False)
    setv_safe(n, a, row_to_set, col - diff, False)

def set_bishop_disallowed_in_col(n, a, row, col, col_to_set):
    diff = abs(col - col_to_set)
    setv_safe(n, a, row + diff, col_to_set, False)
    setv_safe(n, a, row - diff, col_to_set, False)

def place_tower(n, tower, row_free, col_free, row, col):
    setv(n, tower, row, col, True)
    row_free[row] = False
    col_free[col] = False

def place_bishop(n, bishop, bishop_allowed, row, col):
    setv(n, bishop, row, col, True)
    set_bishop_disallowed_in_row(n, bishop_allowed, row, col, 0)
    set_bishop_disallowed_in_row(n, bishop_allowed, row, col, n - 1)

    set_bishop_disallowed_in_col(n, bishop_allowed, row, col, 0)
    set_bishop_disallowed_in_col(n, bishop_allowed, row, col, n - 1)

def try_place_bishop(n, bishop, bishop_allowed, row, col):
    if getv(n, bishop_allowed, row, col):
        place_bishop(n, bishop, bishop_allowed, row, col)

def getch(is_bishop, is_tower):
    if is_tower and is_bishop: return 'o'
    if is_tower and not is_bishop: return 'x'
    if not is_tower and is_bishop: return '+'
    if not is_tower and not is_bishop: return '.'


def print_map(n, bishop, tower):
    for r in range(0, n):
        for c in range(0, n):
            is_bishop = getv(n, bishop, r, c)
            is_tower = getv(n, tower, r, c)
            if is_tower and is_bishop: print('o', end='')
            if is_tower and not is_bishop: print('x', end='')
            if not is_tower and is_bishop: print('+', end='')
            if not is_tower and not is_bishop: print('.', end='')
        print('')

def print_bool_map(n, bmap):
    for r in range(0, n):
        for c in range(0, n):
            if getv(n, bmap, r, c): print('.', end='')
            else: print('-', end='')
        print('')

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(x) for  x in  input().split(" ")]  # read a list of integers, 2 in this case
    old_map = ['.'] * (n * n)
    bishop_allowed = [True] * (n * n)
    bishop = [False] * (n * n)
    tower = [False] * (n * n)
    row_free = [True] * n
    col_free = [True] * n

    for i2 in range(0, m):
        fig, row, col = [x for x in  input().split(" ")]  # read a list of integers, 2 in this case
        row = int(row) - 1
        col = int(col) - 1

        if fig == 'x' or fig == 'o':
            place_tower(n, tower, row_free, col_free, row, col)
        if fig == '+' or fig == 'o':
            place_bishop(n, bishop, bishop_allowed, row, col)


    orig_bishop = list(bishop)
    orig_tower = list(tower)

    # place more towers
    row_free_list = [i for i, x in enumerate(row_free) if x]
    col_free_list = [i for i, x in enumerate(col_free) if x]
    for r, c in zip(row_free_list, col_free_list):
        place_tower(n, tower, row_free, col_free, r, c)

    # place more bishops
    for r in range(0, n):
        if r == 0 or r == n - 1:
            for c in range(0, n):
                try_place_bishop(n, bishop, bishop_allowed, r, c)
        else:
            try_place_bishop(n, bishop, bishop_allowed, r, 0)
            try_place_bishop(n, bishop, bishop_allowed, r, n - 1)


    rating = 0
    change_list = []
    for r in range(0, n):
        for c in range(0, n):
            is_bishop = getv(n, bishop, r, c)
            is_tower = getv(n, tower, r, c)
            is_orig_bishop = getv(n, orig_bishop, r, c)
            is_orig_tower = getv(n, orig_tower, r, c)
            if is_bishop: rating += 1
            if is_tower: rating += 1
            if (is_bishop and not is_orig_bishop) or (is_tower and not is_orig_tower):
                change_list.append((getch(is_bishop, is_tower), r + 1, c + 1))

    print("Case #{}: {} {}".format(i, rating, len(change_list)))
    for (ch, r, c) in change_list:
        print("{} {} {}".format(ch, r, c))
