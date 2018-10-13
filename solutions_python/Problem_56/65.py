def rotate(rows):
    N = len(rows)
    for i in range(N):
        row = []
        for j in range(N):
            row.append(rows[N - j - 1][i])
        yield row

def gravity(rows):
    rows = list(rows)
    N = len(rows)
    cols = []
    for c in range(N):
        col = []
        for r in range(N):
            if rows[r][c] != '.':
                col.append(rows[r][c])
        col = ['.'] * (N - len(col)) + col
        cols.append(col)
    for r in range(N):
        row = []
        for c in range(N):
            row.append(cols[c][r])
        yield row

def print_(rows):
    print '\n'.join(''.join(r) for r in rows)


def winners(K, rows, pos_list):
    last = None
    count = 0
    w = set()
    for r, c in pos_list:
        if rows[r][c] == last:
            count += 1
        else:
            count = 1
        if count == K and rows[r][c] != '.':
            w.add(rows[r][c])
        last = rows[r][c]
    return w

T = int(raw_input())
for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    rows = [raw_input() for n in range(N)]
    rows = list(gravity(rotate(rows)))

    w = set()
    # Rows
    for r in range(N):
        pos_list = [(r, c) for c in range(N)]
        w.update(winners(K, rows, pos_list))

    # Cols
    for c in range(N):
        pos_list = [(r, c) for r in range(N)]
        w.update(winners(K, rows, pos_list))

    # Horiz 1
    for x, y in [(i, 0) for i in range(N)] + [(0, i) for i in range(N)]:
        pos_list = [(x + i, y + i) for i in range(N)
                    if x + i < N and y + i < N]
        w.update(winners(K, rows, pos_list))

    # Horiz 2
    for x, y in [(0, i) for i in range(N)] + [(i, N - 1) for i in range(N)]:
        pos_list = [(x + i, y - i) for i in range(N)
                    if x + i < N and y - i >= 0]
        w.update(winners(K, rows, pos_list))

    if w == set('RB'):
        ans = 'Both'
    elif w == set('R'):
        ans = 'Red'
    elif w == set('B'):
        ans = 'Blue'
    else:
        ans = 'Neither'
    print 'Case #%d: %s' % (t, ans)
