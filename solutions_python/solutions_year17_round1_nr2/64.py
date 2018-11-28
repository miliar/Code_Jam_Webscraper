#
import math


def solve(N, P, servings, packages):
    print N, P, servings, packages
    res = 0
    packages = map(sorted, packages)
    for i in range(N):
        for j in range(P):
            minValue = int(math.ceil(packages[i][j] / 1.1 / servings[i]))
            maxValue = int(packages[i][j] / 0.9 / servings[i])
            packages[i][j] = (minValue, maxValue)
    print packages
    cur = [() for i in range(N)]
    for i in range(N):
        if not cur[i]:
            cur[i] = packages[i].pop()
    while 1:
        print cur
        minValues, maxValues = zip(*cur)
        if max(minValues) <= min(maxValues):
            res += 1
            cur = [() for i in range(N)]
            if not all(packages):
                break
            for i in range(N):
                if not cur[i]:
                    cur[i] = packages[i].pop()
        else:
            worst = cur.index(max(cur))
            if not packages[worst]:
                break
            cur[worst] = packages[worst].pop()
    return res

fi = open('B-large.in', 'r')
fo = open('B-large.out', 'w')
T = int(fi.readline().strip())
for i in xrange(T):
    N, P = map(int, fi.readline().strip().split())
    servings = map(int, fi.readline().strip().split())
    packages = []
    for _ in range(N):
        packages.append(map(int, fi.readline().strip().split()))
    res = solve(N, P, servings, packages)
    out = "Case #%d: %s\n" % (i + 1, res)
    print out
    fo.write(out)
fi.close()
fo.close()
