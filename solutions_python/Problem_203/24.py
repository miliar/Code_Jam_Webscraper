import sys


def all_unknown(row):
    return row == ('?' * len(row))


def fill(row):
    new = []
    skipped = 0
    last = None
    for i, c in enumerate(row):
        if c == '?':
            if last is not None:
                new.append(last)
            else:
                skipped += 1
        else:
            if skipped > 0:
                new.append(skipped * c)
                skipped = 0
            last = c
            new.append(c)
    return ''.join(new)


def solve():
    R, C = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in xrange(R)]
    new = []
    last = None
    skipped = 0
    for r, row in enumerate(grid):
        if all_unknown(row):
            if last is not None:
                new.append(last)
            else:
                skipped += 1
        else:
            this = fill(row)
            if skipped > 0:
                new.extend([this] * skipped)
                skipped = 0
            last = this
            new.append(this)
    for a in new:
        print a


T = int(sys.stdin.readline())
for i in xrange(T):
    print 'Case #%d:' % (i+1)
    solve()
