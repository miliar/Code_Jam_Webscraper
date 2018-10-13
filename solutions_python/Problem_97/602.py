inf = open("C-large.in")
outf = open("C-large.out", "w")

numTests = int(inf.readline().rstrip())

def getNumRecycled(A, B):
    tenPower = 1
    shifts = 0
    while tenPower * 10 <= A:
        shifts += 1
        tenPower *= 10
    res = set()
    for m in range(A, B + 1):
        n = m
        for j in range(shifts):
            d = n // tenPower
            n = (n - d * tenPower) * 10 + d
            if A <= n <= B and n < m:
                res.add((n, m))
    return res

bounds = [ 10 ** p for p in range(7)] + [2000000]
sets = [ getNumRecycled(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1) ] + [set()]

def getNumRecycledFast(A, B):
    index = 0
    while A >= bounds[index + 1]:
        index += 1
    res = 0
    for n, m in sets[index]:
        if A <= n and m <= B:
            res += 1
    return res

for test in range(numTests):
    A, B = map(int, inf.readline().split())
    print("Case #%d: %d" % (test + 1, getNumRecycledFast(A, B)), file=outf)

