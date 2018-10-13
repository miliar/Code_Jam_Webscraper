tn = int(raw_input())
for tc in range(1, tn + 1):
    r, c = tuple(map(int, raw_input().strip().split()))
    m = []
    d = []
    for i in range(r):
        m.append(raw_input().strip())
        d.append([0] * c)
    for i in range(r):
        for j in range(c):
            if m[i][j] != '.':
                d[i][j] |= 0x1
                break
        for j in range(c)[::-1]:
            if m[i][j] != '.':
                d[i][j] |= 0x2
                break
    for j in range(c):
        for i in range(r):
            if m[i][j] != '.':
                d[i][j] |= 0x4
                break
        for i in range(r)[::-1]:
            if m[i][j] != '.':
                d[i][j] |= 0x8
                break
    s = 0
    for i in range(r):
        for j in range(c):
            if m[i][j] != '.':
                if 0 <= s and d[i][j] & (1 << '<>^v'.index(m[i][j])):
                    s += 1
                if d[i][j] == 0xf:
                    s = -1
    if 0 <= s:
        print 'Case #%d: %d' % (tc, s)
    else:
        print 'Case #%d: IMPOSSIBLE' % (tc, )
