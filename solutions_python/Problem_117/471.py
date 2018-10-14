

T = input()
for case in xrange(1, T+1):
    N, M = map(int, raw_input().split())
    field = []
    def is_vertical_series(col, value):
        for r in xrange(N):
            if field[r][col] > value:
                return False
        return True
    
    for _ in xrange(N):
        field.append(map(int, raw_input().split()))
    
    wrong = False
    message = 'YES'
    for i in xrange(N):
        if wrong:
            break
        ma, mi = max(field[i]), min(field[i])
        if ma == mi:
            continue
        for j in xrange(M):
            if field[i][j] < ma:
                if not is_vertical_series(j, field[i][j]):
                    wrong = True
                    break
    if wrong:
        message = 'NO'
    print 'Case #%d: %s' % (case, message)