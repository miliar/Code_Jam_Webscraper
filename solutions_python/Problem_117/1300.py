def solve_case(rows, row_count, col_count):
    row_maxs = map(max, rows)
    col_maxs = map(max, [[row[i] for row in rows] for i in xrange(col_count)])
    for i in xrange(row_count):
        for j in xrange(col_count):
            height = rows[i][j]
            if height != min(row_maxs[i], col_maxs[j]):
                return False
    return True


test_cases = int(raw_input())
for i in xrange(test_cases):
    n, m = map(int, raw_input().split())
    rows = [map(int, raw_input().split()) for j in xrange(n)]
    print 'Case #%d: %s' % (i+1, 'YES' if solve_case(rows, n, m) else 'NO')
