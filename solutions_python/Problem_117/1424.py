T = int(input())

for e in range(T):
    n, m = map(int, input().split())
    a = list()
    cm = list()
    init = [[100] * m] * n
    for x in range(n):
        a.append([int(v) for v in input().split()])
    b = list(zip(*a))  # matrix transpose
    for x in range(n):
        cm = max(a[x])
        init[x] = [cm] * m

    init = list(zip(*init))  # matrix transpose

    for x in range(len(init)):  # be careful -1
        cm = max(b[x])
        init[x] = list(init[x])
        for y in init[x]:
            if y > cm:
                init[x][init[x].index(y)] = cm

    res = list(zip(*init))
    i = 0
    for z in res:
        res[i] = list(z)
        i += 1

    if res == a:
        print('Case #' + str(e+1) + ': YES')
    else:
        print('Case #' + str(e+1) + ': NO')
