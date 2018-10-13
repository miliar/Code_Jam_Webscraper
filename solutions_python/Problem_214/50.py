
def scan(A, i, j, d):  # 0:t 1:r 2:b 3:l
    if d == 0:
        if not i:
            return []
        i -= 1
    elif d == 1:
        if j == len(A[0]) - 1:
            return []
        j += 1
    elif d == 2:
        if i == len(A) - 1:
            return []
        i += 1
    elif d == 3:
        if not j:
            return []
        j -= 1

    c = A[i][j]
    if c == '#':
        return []
    if c == '.':
        res = scan(A, i, j, d)
        if res is not None:
            return [j * len(A) + i] + res
        
def scan2(A, i, j, d):
    r1 = scan(A, i, j, d)
    r2 = scan(A, i, j, d + 2)
    if r1 is not None and r2 is not None:
        return r1 + r2
    
def replace(s, j, c):
    return s[:j] + c + s[j + 1:]


def solve(R, C, A):
    beams, field = [], set()
    for i in xrange(R):
        for j in xrange(C):
            if A[i][j] in '-|':
                beams.append((i, j))
            if A[i][j] == '.':
                field.add(j * len(A) + i)
    select = []
    for b, (i, j) in enumerate(beams):
        r1 = scan2(A, i, j, 0)
        r2 = scan2(A, i, j, 1)
        if r1 is None and r2 is None:
            return False
        if not r1:
            field = field.difference(r2 or [])
            A[i] = replace(A[i], j, '-' if r1 is None or r2 else '|')
        elif not r2:
            field = field.difference(r1 or [])
            A[i] = replace(A[i], j, '|' if r2 is None or r1 else '-')
        else:
            select.append((i, j, r1, r2))
    if not field:
        return A

    cover = {}
    for i, j, v, h in select:
        for x in v:
            cover.setdefault(x, []).append((i, j, 0))
            field.discard(x)
        for x in h:
            cover.setdefault(x, []).append((i, j, 1))
            field.discard(x)
    if field:
        return False

    while cover:
        fixed = [v for v in cover.itervalues() if len(v) <= 1]
        if not fixed:
            break
        if not all(fixed):
            return False
        i, j, d = fixed[0][0]
        A[i] = replace(A[i], j, '-' if d else '|')
        idx = [t for t, x in enumerate(select) if x[:2] == (i, j)][0]
        res = select[idx][2:][d]
        for x in res:
            cover.pop(x, None)
        for k, v in cover.iteritems():
            cover[k] = [x for x in v if x[:2] != (i, j)]
        select.pop(idx)
    if not cover:
        return A
    
    xxx = set(cover.keys())
    for mask in xrange(2 ** len(select)):
        solution = set()
        for bit, item in enumerate(select):
            idx = 2 if (mask & (2 ** bit)) else 3
            solution.update(item[idx])
        if not xxx.difference(solution):
            for bit, (i, j, _, _) in enumerate(select):
                A[i] = replace(A[i], j, '|' if (mask & (2 ** bit)) else '-')
            return A
    

T = int(raw_input())
for t in xrange(T):
    R, C = map(int, raw_input().split(' '))
    A = [raw_input().strip() for i in xrange(R)]
    res = solve(R, C, A)
    print 'Case #%d: %s' % (t + 1, 'POSSIBLE' if res else 'IMPOSSIBLE')
    if res:
        for line in res:
            print line
