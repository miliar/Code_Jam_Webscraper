def rightmost(row):
    rrow = row[:]
    rrow.reverse()
    n = len(row)
    if 1 in rrow:
        return n - 1 - rrow.index(1)
    return -1


def solve(m):
    rows = len(m)
    res = 0

    for row in xrange(rows):
        for row2 in xrange(row, rows):
            ind = rightmost(m[row2])
            if ind <= row:
                temp = m[row2]
                m.pop(row2)
                m.insert(row, temp)
                res += row2 - row
                break

    return res


T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    m = []

    for row in xrange(N):
        m.append(map(lambda x: int(x), raw_input()))

    print 'Case #%d: %d' % (t+1, solve(m))
