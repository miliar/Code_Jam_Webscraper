def b(lawn):
    c_max = [max(r[i] for r in lawn) for i in range(len(lawn[0]))]
    for row in lawn:
        r_max = max(row)
        for i, c in enumerate(row):
            if c < c_max[i] and c < r_max:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    import sys
    cases = int(sys.stdin.readline())
    for tc in range(1, cases+1):
        N, M = map(int, sys.stdin.readline().split())
        lawn = [map(int, sys.stdin.readline().split()) for i in range(N)]
        print 'Case #{0}: {1}'.format(tc, b(lawn))
