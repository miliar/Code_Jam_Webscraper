t = int(raw_input())
for case in range(t):
    n = int(raw_input())
    d = [0] * (n+1)
    l = [0] * (n+1)
    for i in range(n):
        d[i], l[i] = map(int, raw_input().split())
    D = int(raw_input())
    d[n] = D
    l[n] = 0
    f = [-1] * (n+1)
    f[0] = min(l[0], d[0])
    for i in range(n):
        if f[i] >= 0:
            for j in range(i+1, n+1):
                if d[j] - d[i] > f[i]:
                    break
                f[j] = max(f[j], min(l[j], d[j] - d[i]))
    if f[n] >= 0:
        print("Case #%d: YES" % (case + 1))
    else:
        print("Case #%d: NO" % (case + 1))
