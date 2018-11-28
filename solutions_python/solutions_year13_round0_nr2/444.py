def solve(n, m, lawn):
    range_n = range(n)
    range_m = range(m)
    min_row = [max(lawn[i]) for i in range_n]
    min_col = [max(lawn[i][j] for i in range_n) for j in range_m]
    for i in range_n:
        for j in range_m:
            if lawn[i][j] != min(min_row[i], min_col[j]):
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        N, M = [int(k) for k in raw_input().split()]
        lawn = [
            [int(k) for k in raw_input().split()]
            for i in range(N)
        ]
        print 'Case #%d: %s' % (t + 1, solve(N, M, lawn))
