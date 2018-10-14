def rShift(s):
    res = s[1:]
    return res + s[0]

nb = int(raw_input())
for i in range(nb):
    tab = map(int, raw_input().split())
    res = set()
    for j in range(tab[0], tab[1] + 1):
        cur = str(j)
        for k in range(len(cur) - 1):
            cur = rShift(cur)
            curInt = int(cur)
            if curInt >= tab[0] and curInt <= tab[1] and curInt < j:
                res.add((curInt, j))
    print 'Case #{0}: {1}'.format(i + 1, len(res))
