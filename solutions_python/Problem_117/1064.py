T = int(raw_input())

class Test(object):
    def __init__(self, N, M, table):
        self.N = N
        self.M = M
        self.table = table

    def __str__(self):
        return "<Test %dx%d>" % (self.N, self.M)

tests = []
for i in range(T):
    N, M = map(int, raw_input().split(' '))
    table = []
    for n in range(N):
        table.append(map(int, raw_input().split(' ')))
    tests.append(Test(N, M, table))

for t, test in enumerate(tests):
    r_min = [0] * test.N
    c_min = [0] * test.M

    for r, row in enumerate(test.table):
        for c, item in enumerate(row):
            r_min[r] = max(r_min[r], item)
            c_min[c] = max(c_min[c], item)

    result = True

    for r, row in enumerate(test.table):
        for c, item in enumerate(row):
            if item < r_min[r] and item < c_min[c]:
                result = False
                break
        if not result:
            break

    print "Case #%d: %s" % (t + 1, "YES" if result else "NO")
