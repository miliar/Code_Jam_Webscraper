# 0th solution to Problem A

t = int(input())
for a0 in range(t):
    res = None
    rows = []
    r, c = map(int, input().strip().split(' '))
    for a1 in range(r):
        rows.append(list(input().strip()))

    row_empty_arr = [True]*r

    for r, row in enumerate(rows):
        X = 0
        row_empty = True
        last_let = None
        for i, c in enumerate(row):
            if c != "?":
                row_empty = False
                row_empty_arr[r] = False
                for x in range(X, i+1):
                    row[x] = c
                X = i+1
                last_let = c

        if not row_empty:
            for x in range(X, len(row)):
                row[x] = last_let

        if not row_empty:
            R = r-1
            while R >= 0 and rows[R][0] == "?":
                rows[R] = rows[r]
                R -= 1

    if row_empty_arr[-1]:
        Y = len(rows)-1
        while row_empty_arr[Y]:
            Y -=1
        YYY = Y
        while Y < len(rows)-1:
            Y += 1
            rows[Y] = rows[YYY]

    print("Case #" + str(a0 + 1) + ": ")
    for row in rows:
        print("".join(row))
