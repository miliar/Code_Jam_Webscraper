def solve(n, p):
    p2 = {}
    value = 0

    row = [True] * n
    col = [True] * n
    d1 = [True] * (2 * n - 1)
    d2 = [True] * (2 * n - 1)
    for i, j in p:
        t = p[(i, j)]
        if t == "x" or t == "o":
            row[i] = False
            col[j] = False
            value += 1
        if t == "+" or t == "o":
            d1[i + j] = False
            d2[i - j] = False
            value += 1

    for i in range(n):
        for j in range(n):
            if row[i] and col[j]:
                row[i] = False
                col[j] = False
                value += 1
                t = p.get((i, j))
                if t is not None:
                    p2[(i, j)] = "o"
                else:
                    p2[(i, j)] = "x"

    seq = []
    for i in range(n / 2):
        seq.append(i)
        seq.append(n - i - 1)
    if n % 2 == 1:
        seq.append(n / 2)

    for i in seq:
        for j in seq:
            x = i + j
            y = i - j
            if d1[x] and d2[y]:
                d1[x] = False
                d2[y] = False
                value += 1
                t = p2.get((i, j)) or p.get((i, j))
                if t is not None:
                    p2[(i, j)] = "o"
                else:
                    p2[(i, j)] = "+"
    return value, p2


t = int(raw_input())
for i in range(1, t + 1):
    n, m = map(int, raw_input().strip().split())
    p = {}
    for j in range(m):
        ch, r, c = raw_input().strip().split()
        p[(int(r) - 1, int(c) - 1)] = ch
    value, points = solve(n, p)
    print("Case #%d: %d %d" % (i, value, len(points)))
    for x, y in points:
        print("%s %d %d" % (points[(x, y)], x + 1, y + 1))
