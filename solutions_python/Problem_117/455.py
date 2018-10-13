
num_cases = input()
for case in range(1, num_cases + 1):
    n, m = [int(t) for t in raw_input().split()]
    board = [set() for i in range(101)]
    for y in range(n):
        row = [int(t) for t in raw_input().split()]
        for x in range(m):
            board[row[x]].add((x, y))
    marked_rows, marked_cols = set(), set()
    failed = False
    for height in range(100, 0, -1):
        if failed:
            break
        coors = board[height]
        curr_used_row, curr_used_col = set(), set()
        for x, y in coors:
            if x in marked_cols and y in marked_rows:
                failed = True
                break
            if x not in marked_cols:
                curr_used_col.add(x)
            if y not in marked_rows:
                curr_used_row.add(y)
        marked_rows = marked_rows.union(curr_used_row)
        marked_cols = marked_cols.union(curr_used_col)
    if failed:
        print "Case #%d: NO" % case
    else:
        print "Case #%d: YES" % case