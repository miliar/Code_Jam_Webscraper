import sys
sys.setrecursionlimit(10000)


def read_ints():
    a = raw_input().split()
    return [int(x) for x in a]


def read_int():
    return read_ints()[0]


def solve():
    N, M = read_ints()
    lawn = [read_ints() for i in range(N)]
    max_row = [max(row) for row in lawn]
    max_col = [max(row[i] for row in lawn) for i in range(M)]
    for y in range(N):
        for x in range(M):
            if lawn[y][x] < max_row[y] and lawn[y][x] < max_col[x]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())
