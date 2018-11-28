import sys

input = sys.stdin.read().split()
def pop_int():
    return int(input.pop(0))

def first(A):
    for i, a in enumerate(A):
        if a != '.':
            return i
    return len(A)

for t in xrange(pop_int()):
    R = pop_int()
    C = pop_int()
    field = [input.pop(0) for i in xrange(R)]

    row_coverage = []
    col_coverage = []

    for row in field:
        for i, ch in enumerate(row):
            if ch != '.':
                l = i
                break
        else:
            l = C

        for i in xrange(C-1, -1, -1):
            if row[i] != '.':
                r = i
                break
        else:
            r = -1

        row_coverage.append((l, r))

    for c in xrange(C):
        for i in xrange(0, R):
            if field[i][c] != '.':
                l = i
                break
        else:
            l = R

        for i in xrange(R-1, -1, -1):
            if field[i][c] != '.':
                r = i
                break
        else:
            r = -1

        col_coverage.append((l, r))

    def c():
        res = 0
        for r, row in enumerate(field):
            for c in xrange(C):
                col = row[c]
                if col != '.':
                    if row_coverage[r][0] == c and row_coverage[r][1] == c and col_coverage[c][0] == r and col_coverage[c][1] == r:
                        return 'IMPOSSIBLE'

                if col == '>':
                    if row_coverage[r][1] == c:
                        res += 1
                elif col == '<':
                    if row_coverage[r][0] == c:
                        res += 1
                elif col == 'v':
                    if col_coverage[c][1] == r:
                        res += 1
                elif col == '^':
                    if col_coverage[c][0] == r:
                        res += 1
        return res

    print 'Case #{}: {}'.format(t+1, c())
