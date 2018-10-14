MAX = 1000
inf = open("b.in", "r")
ouf = open("b.out", "w")
T = int(inf.readline())
for t in range(T):
    print("Case #", (t + 1), ": ", sep="", end="", file=ouf)
    n, m = [int(i) for i in inf.readline().split()]
    a = [[] for i in range(n)]
    for i in range(n):
        a[i] = [int(j) for j in inf.readline().split()]
    while True:
        mi = -1
        mj = -1
        minv = MAX
        for i in range(n):
            for j in range(m):
                if minv > a[i][j]:
                    minv = a[i][j]
                    mi = i
                    mj = j
        if minv == MAX:
            print("YES", file=ouf)
            break
        row = all(a[mi][j] == minv or a[mi][j] == MAX for j in range(m))
        col = all(a[i][mj] == minv or a[i][mj] == MAX for i in range(n))
        if row:
            a[mi] = [MAX for j in range(m)]
        elif col:
            for i in range(n):
                a[i][mj] = MAX
        else:
            print("NO", file=ouf)
            break
inf.close()
ouf.close()