t = int(input())

for i in range(t):
    d, n = map(int, input().split())
    D = float(d)
    mini = -1.0
    for j in range(n):
        di, vi = map(float, input().split())
        if mini < 0 or D / ((D - di) / vi) < mini:
            mini = D / ((D - di) / vi)
    print("Case #%d: %.6f" % (i + 1, mini))
