#/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    inp = open("lawnmower.inp", "r")
    out = open("lawnmower.out", "w")
    tests = int(inp.readline())
    for test in xrange(tests):

        n, m = map(int, inp.readline().strip().split())
        max_row = [0 for x in xrange(n)]
        max_col = [0 for x in xrange(m)]

        matr = []
        for line in xrange(n):
            row = map(int, inp.readline().strip().split())
            max_row[line] = max(row)
            max_col = [max(x, row[idx]) for idx, x in enumerate(max_col)]
            matr.append(row)
        res = True
        for i in xrange(n):
            for j in xrange(m):
                cur = matr[i][j]
                res = res and (cur == max_row[i] or cur == max_col[j])
        out.write("Case #%d: %s\n" % (test + 1, "YES" if res else "NO"))
    out.close()