def row_shape(row):
    out = []
    first_c = None
    for c in row:
        if c != '?':
            first_c = c
            break
    else:
        assert False
    current_c = first_c
    for c in row:
        if c != '?': current_c = c
        out.append(current_c)
    return ''.join(out)

def run_test():
    rc_line = input()
    r, c = map(int, rc_line.split())
    grid = [input() for y in range(r)]
    good_rows = [(y, row) for y, row in enumerate(grid)
                 if any(c != '?' for c in row)]
    last_y = -1
    for cur_y, cur_row in good_rows:
        cur_row_shape = row_shape(cur_row)
        for i in range(cur_y - last_y):
            print(cur_row_shape)
        last_y = cur_y
    for i in range(r - last_y - 1):
        print(cur_row_shape)

for i in range(1, int(input()) + 1):
    print("Case #{}:".format(i))
    run_test()
