nb = int(raw_input())
for i in range(nb):
    tab = map(int, raw_input().split())
    res = 0
    for j in range(tab[0]):
        if tab[2] > tab[3 + j]: continue
        if tab[3 + j] >= tab[2] * 3 - 2:
            res += 1
        elif tab[1] and tab[3 + j] >= tab[2] * 3 - 4:
            res += 1
            tab[1] -= 1
    print "Case #{0}: {1}".format(i + 1, res)
