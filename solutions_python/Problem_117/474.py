t = int(raw_input())

for test in range(1,t+1):
    print "Case #%d:" % test,
    n, m = (int(x) for x in raw_input().strip().split())
    a = [[int(x) for x in raw_input().strip().split()] for i in range(0, n)]
    rows = [max(a[i]) for i in range(0, n)]
    cols = [max([a[i][j] for i in range(0, n)]) for j in range(0, m)]

    res = "YES"
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] != min(rows[i], cols[j]):
                res = "NO"
    print res

