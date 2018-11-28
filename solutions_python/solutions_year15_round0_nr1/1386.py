def solve(tab):
    acc = 0
    res = 0
    for i, val in enumerate(tab[:-1]):
        acc += int(val)
        if acc < i + 1:
            res += i + 1 - acc
            acc += i + 1 - acc
    return res

with open("A-large.in") as f:
    n = int(f.readline())
    for i in range(n):
        smax, tab = f.readline().split(' ')
        res = solve(tab)
        print("Case #%d: " % (i + 1), res)
