tn = int(input())
for test in range(1, tn + 1):
    c, f, x = [float(r) for r in input().split()]
    L = 0
    R = x
    for it in range(100):
        M = (L + R) / 2
        can = True
        t = 0
        s = 2.0
        y = x
        while t + x / s > M:
            if (t + c / s > M):
                can = False
                break
            t = t + c / s
            s += f
        if can:
            R = M
        else:
            L = M
    print("Case #%d: %.7f" % (test, R))
