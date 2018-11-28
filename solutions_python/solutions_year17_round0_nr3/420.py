def naiveSolve(n, k):
    rg = {n: 1}
    for i in range(k):
        area = max(rg)
        if rg[area] > 1:
            rg[area] -= 1
        else:
            del rg[area]
        ls = (area - 1) // 2
        rs = area // 2
        rg[ls] = rg.get(ls, 0) + 1
        rg[rs] = rg.get(rs, 0) + 1
    return (max(ls, rs), min(ls, rs))

def betterSolve(n, k):
    rg = {n: 1}
    i = 0
    while True:
        area = max(rg)
        count = rg[area]
        ls = (area - 1) // 2
        rs = area // 2
        if k-i <= count:
            return (rs, ls)
        else:
            del rg[area]
            rg[ls] = rg.get(ls, 0) + count
            rg[rs] = rg.get(rs, 0) + count
            i += count

n = int(input())
for i in range(n):
    line = input()
    n, k = [int(e) for e in line.split()]
    solution = '%d %d' % betterSolve(n, k)
    print('Case #%d: %s' % (i+1, solution))
