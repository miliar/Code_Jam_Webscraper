T = int(input())
for t in range(1, T+1):
    r, c = map(int, input().split())
    rows = []
    for i in range(0, r):
        row = list(input())
        rows.append(row)

    for row in rows:
        for i in range(1, c):
            if row[i] == '?':
                row[i] = row[i-1]
        for i in range(c-2, -1, -1):
            if row[i] == '?':
                row[i] = row[i+1]

    for i in range(1, r):
        if rows[i][0] == '?':
            rows[i] = rows[i-1]

    for i in range(r-2, -1, -1):
        if rows[i][0] == '?':
            rows[i] = rows[i+1]
    print("Case #{0}:".format(t))
    for row in rows:
        print("".join(row))
