def solve(lawn, initial=100):

    if len(lawn) == 1 or len(lawn[0]) == 1:
        return True

    col_highest = [max(l) for l in zip(*lawn)]

    for row in lawn:
        highest = max(row)
        for x, h in enumerate(row):
            if h not in [highest, col_highest[x]]:
                return False

    return True


if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n, m = map(int, raw_input().split(" "))
        lawn = [map(int, raw_input().split(" ")) for _ in range(n)]
        print "Case #%d: %s" % (i+1, "YES" if solve(lawn) else "NO")