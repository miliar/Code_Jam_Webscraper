ncases = int(raw_input())
for caseno in xrange(1, ncases+1):
    n, m = map(int, raw_input().split())
    pattern = []
    for i in xrange(n):
        row = map(int, raw_input().split())
        assert len(row) == m
        pattern.append(row)

    # calculate the height at which lawnmower *should* cut for each row/column
    rowmax = [max(row) for row in pattern]
    colmax = [max(row[j] for row in pattern) for j in xrange(m)]

    # verify if the pattern arises from those heights
    result = True
    for i in xrange(n):
        for j in xrange(m):
            if pattern[i][j] != min(rowmax[i], colmax[j]):
                result = False
                break

    if result:
        print 'Case #%d: YES' % caseno
    else:
        print 'Case #%d: NO' % caseno

