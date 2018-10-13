t = int(input())

for c in range (1, t + 1):
    d, n = raw_input().split()

    d = float(d)
    n = int(n)

    m = -1
    for i in range(n):
        k, s = raw_input().split()
        k = float(k)
        s = float(s)
        if m < 0 or (d - k) / s > m:
            m = (d - k) / s

    r = d / m

    print("Case #{}: {}".format(c, r))
