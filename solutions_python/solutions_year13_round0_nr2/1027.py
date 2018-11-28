"Lawnmower: https://code.google.com/codejam/contest/2270488/dashboard#s=p1"


def solve(lawn, n, m):
    rows = lawn[:]
    cols = zip(*lawn)
    for i in range(n):
        for j in range(m):
            curr = lawn[i][j]
            if any(c > curr for c in rows[i]) and \
            any(c > curr for c in cols[j]):
                return 'NO'
    return 'YES'


def main():
    t = int(raw_input())
    for i in range(t):
        n, m = map(int, raw_input().split())
        lawn = [map(int, raw_input().split()) for _ in range(n)]
        res = solve(lawn, n, m)
        print "Case #%d: %s" % (i + 1, res)


if __name__ == "__main__":
    main()
